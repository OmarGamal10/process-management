#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/wait.h>

int main(int argc, char *argv[]){
  char *path = argv[1];
  int numTAs = atoi(argv[2]);
  int passingGrade = atoi(argv[3]);
  int numStudents;
  FILE *fptr = fopen(path, "r");
  fscanf(fptr, "%d", &numStudents);
  int **grades = (int **)malloc(numStudents * sizeof(int *));
  for(int i = 0; i < numStudents; ++i){
    grades[i] = (int *)malloc(2 * sizeof(int));
    fscanf(fptr, "%d %d", &grades[i][0], &grades[i][1]);
  }
  fclose(fptr);
  pid_t pids[numTAs];
  for(int i = 0; i < numTAs; ++i){
    pids[i] = fork();
    int numPassed = 0;
    if(pids[i] == 0){
      int partition = numStudents / numTAs;
      int diff = numStudents % numTAs;
      for(int j = i * partition; j < (i == numTAs - 1 && (diff || numStudents < numTAs) ? numStudents : (i + 1) * partition) ; ++j){
        if(grades[j][0] + grades[j][1] >= passingGrade){
          numPassed++;
        }
      }
      for(int j = 0; j < numStudents; ++j)
        free(grades[j]);
      free(grades);
      exit(numPassed); // we can hope that the number of students passed per group will be less than 256 :)
    }
  }
  if(pids[0] >= 0){
    for(int i = 0; i < numTAs; ++i){
      int status;
      waitpid(pids[i], &status, 0);
      printf("%d", status >> 8);
      if(i != numTAs - 1)
        printf(" ");
    }
  }
  for(int i = 0; i < numStudents; ++i)
    free(grades[i]);
  free(grades);
  return 0;
}

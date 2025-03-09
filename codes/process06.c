#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

int main()
{
	int pid, stat_loc;

	printf("\nmy pid = %d\n", getpid());
	pid = fork();

	if (pid == -1)
		perror("error in fork");

	else if (pid == 0)
	{
		printf("\nI am the child, my pid = %d and my parent's pid = %d\n\n", getpid(), getppid());
		// execl("/mnt/c/Lab3/Codes/hello", "hello", "Muhammad", NULL);
		execl("/bin/ps", "ps", "-l", NULL);
		printf("This line will not be printed");
	}
	else
	{
		printf("\nI am the parent, my pid = %d and my parent's pid = %d\n\n", getpid(), getppid());
		pid = wait(&stat_loc);
	}

	printf("\nPID %d terminated\n\n", getpid());
	return 0;
}

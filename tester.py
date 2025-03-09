import subprocess
import os
import tempfile
import shutil

def compile_program():
    print("🛠️  Compiling OmarGamal_9230597.c ...")
    result = subprocess.run(["gcc", "OmarGamal_9230597.c", "-o", "OmarGamal_9230597.o"], capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ Compilation failed:")
        print(result.stderr)
        exit(1)
    print("✅ Compilation successful.\n")

def run_test(test_file, num_TAs, pass_grade, expected_output):
    result = subprocess.run(["./OmarGamal_9230597.o", test_file, str(num_TAs), str(pass_grade)], capture_output=True, text=True)
    output = result.stdout.strip()
    return output == expected_output, output, result.stderr

def main():
    compile_program()
    
    tests = [
        {
            "name": "test1",
            "contents": "5\n30 25\n20 15\n40 20\n10 20\n25 30\n",
            "TAs": 2,
            "pass_grade": 50,
            "expected": "1 2"
        },
        {
            "name": "test2",
            "contents": "4\n30 40\n20 30\n25 35\n10 20\n",
            "TAs": 4,
            "pass_grade": 60,
            "expected": "1 0 1 0"
        },
        {
            "name": "test3",
            "contents": "6\n50 40\n60 45\n40 70\n20 30\n55 50\n45 55\n",
            "TAs": 3,
            "pass_grade": 100,
            "expected": "1 1 2"
        },
        {
            "name": "test4",
            "contents": "1\n10 15\n",
            "TAs": 3,
            "pass_grade": 20,
            "expected": "0 0 1"
        },
        {
            "name": "test5",
            "contents": "10\n30 30\n40 40\n20 30\n50 40\n35 45\n25 55\n30 50\n10 10\n40 30\n45 40\n",
            "TAs": 3,
            "pass_grade": 80,
            "expected": "1 3 2"
        },
        {
            "name": "test6",
            "contents": "7\n10 15\n20 10\n30 0\n25 0\n15 15\n20 15\n10 20\n",
            "TAs": 2,
            "pass_grade": 20,
            "expected": "3 4"
        },
        {
            "name": "test7",
            "contents": "5\n10 20\n30 40\n20 30\n15 15\n25 20\n",
            "TAs": 2,
            "pass_grade": 100,
            "expected": "0 0"
        },
        {
            "name": "test8",
            "contents": "8\n10 10\n20 10\n0 25\n15 15\n20 5\n5 5\n10 20\n0 0\n",
            "TAs": 4,
            "pass_grade": 25,
            "expected": "1 2 1 1"
        },
        {
            "name": "test9",
            "contents": "9\n50 50\n49 50\n60 50\n30 30\n40 60\n55 50\n20 20\n70 40\n50 25\n",
            "TAs": 3,
            "pass_grade": 100,
            "expected": "2 2 1"
        },
        {
            "name": "test10",
            "contents": "12\n30 40\n20 30\n40 40\n35 35\n50 10\n25 50\n60 15\n20 40\n45 30\n30 20\n55 20\n40 40\n",
            "TAs": 5,
            "pass_grade": 70,
            "expected": "1 2 1 1 3"
        }
    ]
    
    total_tests = len(tests)
    passed_tests = 0
    failed_tests = []
    
    temp_dir = tempfile.mkdtemp()
    print("🚀 Running test cases...\n")
    for test in tests:
        test_file_path = os.path.join(temp_dir, f"{test['name'].replace(' ', '_')}.txt")
        with open(test_file_path, "w") as f:
            f.write(test["contents"])
        print(f"🔍 Running {test['name']}...")
        success, output, stderr = run_test(test_file_path, test["TAs"], test["pass_grade"], test["expected"])
        if success:
            print(f"✅ {test['name']} PASSED. Output: {output}\n")
            passed_tests += 1
        else:
            print(f"❌ {test['name']} FAILED.")
            print(f"   Expected: {test['expected']}")
            print(f"   Got     : {output}")
            if stderr:
                print("   stderr  :", stderr)
            print()
            failed_tests.append(test["name"])

    print(f"✅ Passed: {passed_tests}")
    
    if (total_tests - passed_tests) > 0:
      print(f"❌ Failed: {total_tests - passed_tests} ({', '.join(failed_tests)})")
    else:
      print(f"❌ Failed: 0")
      
    if failed_tests:
        print("❌ Some tests failed.")
    else:
        print("🎉 All tests passed successfully!")
    
    shutil.rmtree(temp_dir)
    if os.path.exists("OmarGamal_9230597.o"):
        os.remove("OmarGamal_9230597.o")

if __name__ == "__main__":
    main()

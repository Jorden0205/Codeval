import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip().split(" ")
        test = test[::-1]
        print(" ".join(test))

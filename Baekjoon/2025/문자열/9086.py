import sys

t = int(sys.stdin.readline())

for i in range(t):
    string = sys.stdin.readline()
    print(string[0]+string.strip()[-1])


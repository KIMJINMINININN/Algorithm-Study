import sys

n = int(sys.stdin.readline())
string = sys.stdin.readline().strip()

sum = 0
for i in string:
    sum += int(i)

print(sum)
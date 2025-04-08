import sys

numList = []
for i in range(10):
    n = int(sys.stdin.readline())
    numList.append(n % 42)

result1 = set(numList)
print(len(result1))
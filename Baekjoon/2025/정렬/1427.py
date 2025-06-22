import sys

input = sys.stdin.readline
n = int(input())

nList = list(str(n))
nList.sort(reverse=True)

result = "".join(nList)
print(result)
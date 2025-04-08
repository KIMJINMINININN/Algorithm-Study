import sys

n, x = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

myList = []
for i in a:
    if i < x:
        myList.append(i)

for j in myList:
    print(j, end=" ")
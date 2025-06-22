import sys
input = sys.stdin.readline

n = int(input())
myList = []

for i in range(0, n):
    myList.append(int(input()))

temp = sorted(myList)

for i in temp:
    print(i)
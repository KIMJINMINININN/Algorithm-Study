n = int(input())

nList = []

for i in range(0, n):
    num = int(input())
    nList.append(num)

nList.sort()

for i in nList:
    print(i)
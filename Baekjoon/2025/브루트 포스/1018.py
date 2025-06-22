n, m = map(int,input().split())
myList = []

for i in range(n):
    inList = list(map(int, input().split()))
    myList.append(inList)

print(myList)

for i, item in enumerate(myList):
    for j, jItem  in enumerate(item):
        if i > 0 and i < n and j > 0 and j < m:

#위:[x, y-1]
#왼:[x-1, y]
#오른:[x+1, y]
#아래:[x, y+1]
n = int(input())
myList = []
for i in range(n):
    a, b = map(int,input().split())
    myList.append((a, b))

maxX, maxY, minX, minY = -10001, -10001, 10001, 10001

for i in myList:
    if maxX < i[0]:
        maxX = i[0]

    if maxY < i[1]:
        maxY = i[1]

    if minX > i[0]:
        minX = i[0]

    if minY > i[1]:
        minY = i[1]

value = abs(maxX - minX) * abs(maxY - minY)
print(value)
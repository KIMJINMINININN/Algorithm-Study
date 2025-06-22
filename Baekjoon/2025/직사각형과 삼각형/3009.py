x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

maxX = max([x1, x2, x3])
maxY = max([y1, y2, y3])
minX = min([x1, x2, x3])
minY = min([y1, y2, y3])

myList = [[x1, y1], [x2, y2], [x3, y3]]
result = [[maxX, maxY], [maxX, minY], [minX, minY], [minX, maxY]]

# 컴프리헨션
missing1 = [pt for pt in myList if pt not in result]
print(missing1)
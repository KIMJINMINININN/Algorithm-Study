nList = []
avg = 0
middle = 0
for i in range(0, 5):
    num = int(input())
    nList.append(num)

nList.sort()

for index, item in enumerate(nList):
    avg += int(item)
    if index == 2:
        middle = item

print(int(avg / 5))
print(middle)


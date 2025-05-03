a = []
maxValue = 0
maxHang, maxEuer = 0, 0

for i in range(9):
    temp = list(map(int, input().split()))
    a.append(temp)


for idx, val in enumerate(a):
    for inIdx, inVal in enumerate(val):
        if inVal > maxValue:
            maxHang = idx
            maxEuer = inIdx
            maxValue = inVal

print(maxValue)
print(maxHang+1, maxEuer+1)

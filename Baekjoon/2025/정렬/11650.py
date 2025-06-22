import sys

input = sys.stdin.readline
# 계수정렬 활용
n = int(input())

nList = []
copyList = nList


for i in range(0, n):
    inList = list(map(int,input().split()))
    nList.append(inList)

print(nList)
print(copyList)

for indexA, itemA in enumerate(nList):
    for indexB, itemB in enumerate(nList):
        if indexA != indexB:
            if itemA[indexA] > itemB[indexB]:
                copyList[indexA] = itemB
                copyList[indexB] = itemA



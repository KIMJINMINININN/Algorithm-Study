import sys
input = sys.stdin.readline  # 입력 속도를 높여주는 sys.stdin.readline을 input으로 사용합니다.

ndict = {}
resultList = []

n = int(input())
nList = list(map(int, input().split()))

m = int(input())
mList = list(map(int, input().split()))

for nNum in nList:
    ndict[nNum] = nNum

for mNum in mList:
    if mNum in ndict:
        resultList.append(str(1))
    else:
        resultList.append(str(0))

resultList = " ".join(resultList)
print(resultList)


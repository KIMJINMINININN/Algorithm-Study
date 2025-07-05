import sys
input = sys.stdin.readline  # 입력 속도를 높여주는 sys.stdin.readline을 input으로 사용합니다.

n, m = map(int, input().split())
nList = []
mList = []

count = 0

for i in range(0, n):
    nList.append(str(input().strip()))

for j in range(0, m):
    mList.append(str(input().strip()))

for mValue in mList:
    if mValue in nList:
        count += 1

# for nValue in nList:
#     for mValue in mList:
#         if nValue == mValue:
#             count += 1
#             continue

print(count)
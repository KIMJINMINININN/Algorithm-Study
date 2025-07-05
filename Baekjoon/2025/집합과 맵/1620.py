import sys
input = sys.stdin.readline  # 입력 속도를 높여주는 sys.stdin.readline을 input으로 사용합니다.

n, m = map(int,input().split())
picDic = {}
requestList = []

for i in range(0, n):
    name = input().strip()
    picDic[i + 1] = name

for j in range(0, m):
    value = input().strip()
    if value.isdigit():
        requestList.append(int(value))
    else:
        value = value.strip()
        requestList.append(value)

bb = {v: k for k, v in picDic.items()}  # // {'AA': '0', 'BB': '1', 'CC': '2'}
for value in requestList:
    if str(type(value)) == "<class 'int'>":
        print(picDic[value])
    else:
        print(bb.get(value))

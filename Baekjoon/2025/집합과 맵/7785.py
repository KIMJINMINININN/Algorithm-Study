import sys
input = sys.stdin.readline  # 입력 속도를 높여주는 sys.stdin.readline을 input으로 사용합니다.

n = int(input())
personDic = {}

for i in range(0, n):
    name, status = input().split()
    # 들어왔을때
    if status == "enter":
        personDic[name] = name
    # 나갔을때
    elif status == "leave":
        del personDic[name]

dicKeys = [*personDic]
dicKeys.sort(reverse=True)
for value in dicKeys:
    print(value)


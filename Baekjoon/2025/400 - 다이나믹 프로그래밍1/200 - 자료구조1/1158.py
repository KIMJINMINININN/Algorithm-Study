import sys
input = sys.stdin.readline

n, k = map(int,input().split())
myList = []
index = 0
result = []

for i in range(1, n+1):
    myList.append(i)

while myList:
    # 매번 현재 남은 길이로 모듈로 연산
    index = (index + k - 1) % len(myList)
    # 뽑아서 결과에 추가
    result.append(str(myList.pop(index)))
    # if len(myList) < index + k - 1:
    #     index = (index + k - 1) % len(myList)
    #     if len(myList) == 0:
    #         break
    #     elif len(myList) < index:
    #         continue
    #     elif len(myList) == index:
    #         index = 0
    # else:
    #     index = index + k - 1
    #
    # # 3번째 삭제
    # result.append(str(myList[index]))
    # del myList[index]

result = ", ".join(result)
print("<"+result+">")



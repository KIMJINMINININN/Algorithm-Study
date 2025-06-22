import sys
input = sys.stdin.readline  # 입력 속도를 높여주는 sys.stdin.readline을 input으로 사용합니다.

n = int(input())
myList = []
result = []

for i in range(0, n):
    text = input()
    myList.append(text.strip())

# 중복 제거
myList = set(myList)  # 중복을 제거하기 위해 리스트를 집합으로 변환합니다.
myList = list(myList)  # 중복이 제거된 집합을 다시 리스트로 변환합니다.

myList.sort()
# 문자열 길이로 정렬
myList.sort(key=len)

# for i in range(0, n):
#     for j in range(i, n):
#         if len(myList[i]) > len(myList[j]):
#             temp = myList[i]
#             myList[i] = myList[j]
#             myList[j] = temp

# for i in myList:
#     if i not in result:  # 해당 데이터가 없다면 추가해주고, 이미 존재한다면 넘어간다.
#         result.append(i)

for i in myList:
    print(i)


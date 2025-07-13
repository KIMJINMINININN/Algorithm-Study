# import sys
# input = sys.stdin.readline
# n = int(input())
# myList = list(map(int, input().split()))
# okunList = []
#
# for index, item in enumerate(myList):
#     while True:
#         if index == len(myList):
#             break
#         else:
#             if item < myList[index]:
#                 okunList.append(str(myList[index]))
#                 break
#             elif index == len(myList) - 1:
#                 okunList.append("-1")
#             index += 1
#
# sys.stdout.write(" ".join(okunList))


import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = [-1] * n
stack = []

for i, x in enumerate(arr):
    # 스택에 남은 인덱스 중, arr[idx] < x 면 답을 x 로 채우고 pop
    while stack and arr[stack[-1]] < x:
        ans[stack.pop()] = x
    stack.append(i)

print(" ".join(map(str, ans)))

#Index:  0   1   2   3   4
#Value: [3,  5,  2,  7,  5]
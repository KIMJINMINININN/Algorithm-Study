import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = [-1] * n
stack = []
max_val = max(arr)
arrcount = [0] * (max_val + 1)

for i, x in enumerate(arr):
    arrcount[x] += 1

for i, x in enumerate(arr):
    # 스택에 남은 인덱스 중, arr[idx] < x 면 답을 x 로 채우고 pop
    while stack and arrcount[arr[stack[-1]]] < arrcount[x]:
        ans[stack.pop()] = x
    stack.append(i)

print(" ".join(map(str, ans)))
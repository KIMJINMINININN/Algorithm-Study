# X
# for j in (i+1, i-1, 2*i) 이런방법으로도 사용할수있군
from collections import deque

limit = 100001

def solve(arr, n, k):
    q = deque()
    q.append(n)
    while q:
      # print("q : ", q)
      i = q.popleft()
      # print("i : ", i)
      if i == k:
        return arr[i]
      for j in (i+1, i-1, 2*i):
        # print("  j : ", j)
        # 범위안에 들어가면 ㅇㅋ , arr[j] == 0은 한번했던것은 다시하지않게하기위해
        if (0 <= j < limit) and arr[j] == 0: 
          # print(f"  arr[i] : ", arr[i])
          arr[j] = arr[i] + 1
          # print(f"  arr[j] : ", arr[j])
          q.append(j)

n, k = map(int, input().split())
# find = [x for x in range(0,100001)] 이렇게도 아래와 같은 결과를 나타낼수있다.
find = [0] * limit
print(solve(find, n, k)) 
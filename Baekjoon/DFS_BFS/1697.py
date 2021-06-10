# 숨바꼭질
''' 
n, k = 
graph = [x for x in range(0,100001)]
# print("graph : ", graph)

def dfs(x):
if x <= -1 or x >= n or y <= -1 or y >= n:
  return False
if graph[x] == 1:
  graph[x][y] = 0
  dfs(x - 1)
  dfs(x + 1)
  dfs(2x)
  return True
return False

for i in range(test_case):
n , m , k = map(int,input().split())
graph = [[0] * (n+1) for i in range(n+1)]

for _ in range(k):
  a, b = map(int,input().split())
  graph[a] = 1

result = 0
for i in range(n):
    if dfs(i) == True:
      result += 1   
'''
# ---------------------------------------------

''' 
while(True):
  if x > k:
    if_roof(x, k)
  elif x < k:
    if_roof(x, k)
  break

def if_roof(x, k):
  if 2x > k:
    if (2x - k) > (k - x):
      continue
    elif ((2x - k) == (k - x)) && ((2x - k) < (k - x)):
      x = x * 2
    else:
      x = x + 1
      # x = x - 1
  else:
    x = x * 2 
  return x
 '''
# ---------------------------------------------
# for j in (i+1, i-1, 2*i) 이런방법으로도 사용할수있군
from collections import deque

limit = 100001

def solve(arr, n, k):
    q = deque()
    q.append(n)
    while q:
      # print("q : ", q)
      i = q.popleft()
      print("i : ", i)
      if i == k:
        return arr[i]
      for j in (i+1, i-1, 2*i):
        print("  j : ", j)
        # 범위안에 들어가면 ㅇㅋ
        if (0 <= j < limit) and arr[j] == 0: 
          print(f"  arr[i] : ", arr[i])
          arr[j] = arr[i] + 1
          q.append(j)

n, k = map(int, input().split())
# find = [x for x in range(0,100001)] 이렇게도 아래와 같은 결과를 나타낼수있다.
find = [0] * limit
print(solve(find, n, k))

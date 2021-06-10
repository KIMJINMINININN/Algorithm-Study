# 토마토
from collections import deque
n, m, h = map(int, input().split())
s = []
queue = deque()
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
## 데이터 

for j in range(h):
  # print("j :", j)
  s_temp = []
  for i in range(m):
      # print("i : ", i)
      s_temp.append(list(map(int, input().split())))
      # print("s_temp : ", s_temp)
  s.append(s_temp)
  # print("s : ", s)


def bfs():
    while queue:
        c, b, a = queue.popleft()
        # print(f"a : {a}, b : {b}, c : {c}")
        for i in range(6):
          x = a + dx[i]
          y = b + dy[i]
          z = c + dz[i]
          # print(f"x : {x}, y : {y}, z : {z}")
          if 0 <= x < n and 0 <= y < m and 0 <= z < h and s[z][y][x] == 0:
            # print("여기에 안오는거같은데 오나??")
            s[z][y][x] = s[c][b][a] + 1
            queue.append([z, y, x])
            # print("queue : ", queue)
for t in range(h):
  # print("t : ", t)
  for j in range(m):
    # print("  j : ", j)
    for i in range(n):
      # print(" i : ", i)
      # print("s[t][j][i] : ", s[t][j][i])
      if s[t][j][i] == 1:
        queue.append([t, j, i])

# print("queue : ", queue)
# print("s1 : ", s)
# print("queue1 : ", queue)

bfs()

# print("@@@ s2 : ", s)
# print("@@@ queue2 : ", queue)

isTrue = False
result = -2
for t in s:
  for i in t:
    # print("i : ", i)
    for j in i:
      # print("j : ", j)
      if j == 0:
          isTrue = True
      result = max(result, j)
        # print("in result : ", result)
# print("result : ", result)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)
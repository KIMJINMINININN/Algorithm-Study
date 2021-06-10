## 토마토

from collections import deque
m, n = map(int, input().split())
s = []
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    s.append(list(map(int, input().split())))


def bfs():
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and s[x][y] == 0:
                s[x][y] = s[a][b] + 1
                queue.append([x, y])
                # print("queue : ", queue)
for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            queue.append([i, j])

# print("s1 : ", s)
# print("queue1 : ", queue)

bfs()

# print("@@@ s2 : ", s)
# print("@@@ queue2 : ", queue)

isTrue = False
result = -2
for i in s:
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
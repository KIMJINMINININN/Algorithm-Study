''' INF = int(1e9)

n = int(input())

# graph = [[INF] * (n + 1) for _ in range(n + 1)]
temp_graph = [[INF] * (n + 1) for _ in range(n + 1)]
# temp_graph[0] = [INF] * 4
for i in range(1, n + 1):
  temp_list = list(map(int,input().split()))
  # print(temp_list)
  for j in range(1, n + 1):
    temp_graph[i][j] = temp_list[j - 1]

print(temp_graph)

for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      temp_graph[i][j] = min(temp_graph[i][j], temp_graph[i][k] + temp_graph[k][j])

print(temp_graph) '''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1 , 0]
dy = [0 , 1, 0 , -1]

for _ in range(int(input())):
  n = int(input())
  graph = []
  
  for i in range(n):
    graph.append(list(map(int, input().split())))
  
  distance = [[INF] * n for _ in range(n)]
  x, y = 0
  q = [(graph[x][y], x, y)]
  distance[x][y] = graph[x][y]

  while q:
    dist, x, y = heapq.heappop(q)
    if distance[x][y] < dist:
      continue
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      cost =  dist + graph[nx][ny]
      if cost < distance[nx][ny]:
        distance[nx][ny] = cost
        heapq.heappush(q, (cost, nx, ny))

  print(distance[n - 1][n - 1])


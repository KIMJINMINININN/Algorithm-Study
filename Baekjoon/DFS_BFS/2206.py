# # 벽 부수고 이동하기
# from collections import deque
 
# n, m = map(int,input().split())
# graph = []
# for i in range(n):
#   graph.append(list(map(int,input())))

# # print("my_list : ", my_list)

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def bfs(a, b):
#   queue = deque()
#   queue.append([a, b])
#   x, y = queue.popleft()
#   while(queue):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if x < 0 and x >= n and y < 0 and y >= m:
#           continue
#         if graph[nx][ny] == 1:
#           continue
#         if graph[nx][ny] == 0:
#           graph[nx][ny] = graph[x][y] + 1
#           queue.append((nx, ny))
#     # 가장 오른쪽 아래까지의 최단 거리 반환
#   if graph[n - 1][m - 1] == 0:
#     return -1
#   else:
#     return graph[n - 1][m - 1]

   
# print(bfs(0, 0))

# 미로 탐색
from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph):
  # 큐 구현을 위해 deque 라이브러리 사용
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    # 현재 위치에서 네 방향으로 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 1:
        continue
      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  # 가장 오른쪽 아래까지의 최단 거리 반환
  if graph[n - 1][m - 1] == 0:
    return -1
  else:
    return graph[n - 1][m - 1] + 1

one_list = []
value_list = []
for (i, numi) in enumerate(graph):
  for (j, numj) in enumerate(numi):
    if numj == 1:
      one_list.append([i, j])

for (i, num) in enumerate(one_list):
  x, y = num
  copy_graph = graph
  copy_graph[x][y] = 0
  bfs(x, y, copy_graph)
  value_list.append(bfs(x, y, copy_graph))
print("value_list : ", value_list)
# print(bfs(0, 0))

# 
n, m = map(int,input().split())
INF = int(1e9)

graph = [[INF] * (n + 1) for i in range(n + 1)]

# 자기에게로 가는 경로는 0으로 만들어주기
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

# 값을 입력받아서 해당 거리 정보 넣어주기
for _ in range(m):
  a, b = map(int, input().split())
  # 양뱡향
  graph[a][b] = 1
  graph[b][a] = 1

# 거치는 곳 : x , 가야하는곳 k
k, x = map(int,input().split())

for x in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# k까지의 최소거리
value = graph[1][k] + graph[k][x]

if value >= INF:
  print(-1)
else:
  print(value)
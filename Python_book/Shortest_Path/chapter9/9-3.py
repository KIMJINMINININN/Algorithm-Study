''' INF = int(1e9) # 무한값 설정

# 노드개수 및간선의 개수 입력
n = int(input())
m = int(input())

# 2차원 리스트 만들고 모든값 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  # A에서 B로 가는 비용 C라고 설정
  a, b, c = map(int, input().split())
  graph[a][b] = c
print("@@@@@@graph :", graph)

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
  print("1. @k : ", k)
  for a in range(1, n + 1):
    print("2. @@a : ", a)
    for b in range(1, n + 1):
      print("3. @@@b : ", b)
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
  
# 결과 출력
for a in range(1, n + 1):
  for b in range(1, n + 1):
    # 도달할수 없는 경우, 무한이라고 출력
    if graph[a][b] == INF:
      print("INFINITY", end=" ")
    else:
      print(graph[a][b], end=" ")

  print()

 '''

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c

for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(1, n + 1):
  for b in range(1, n + 1):
    if graph[a][b] == INF:
      print("무한!")
    else:
      print(graph[a][b], end=" ")
  print()
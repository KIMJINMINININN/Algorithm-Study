# 백준 11404 플로이드
''' 
import heapq
INF = int(1e9)
n = int(input())
m = int(input())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

# graph 초기 세팅
for _ in range(m):
  a, b, c = map(int,input().split())
  graph[a].append((b,c))

print(distance)
print(graph)

# 다이제스트라 함수 구현
def dks(start):
  heapq.heappush(q, (0, sta))
  print("dks") 
'''
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for i in range(n + 1)]

for _ in range(m):
  a, b, c = map(int,input().split())
  if c < graph[a][b]:
    graph[a][b] = c

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if i == j:
      graph[i][j] = 0

# 플로이드 알고리즘
for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      graph[i][j] = min(graph[i][j] , graph[i][k] + graph[k][j])

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if graph[i][j] == INF:
      print(0, end=" ")
    else:
      print(graph[i][j], end=" ")
  print()
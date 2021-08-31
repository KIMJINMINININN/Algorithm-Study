''' import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
# 노드 연결되어있는 노드에 대한 정보 담는 리스트
graph = [[] for i in range(n + 1)]
# 최단 거리 나타내기
distance = [INF] * (n + 1)

# a : 노드 , b : b번노드 , c : 거리

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

print("@@@@@graph : ", graph)
print("@@@@@distance : ", distance)

def dijkstra(start):
  q = []
  # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q: # 큐가 비어있지 않으면
    print("#############q :", q)
    #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heapq.heappop(q)
    print(f"dist : {dist} now : {now}")
    #현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if distance[now] < dist:
      continue
    #현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      # print("graph[now]  : " , graph[now])
      # print("i  : " , i)
      # print("i[1]  : " , i[1])
      cost = dist + i[1]

      print(f"graph[now] {graph[now]}")
      print(f"dist {dist} + i[1] {i[1]}")
      print(f"cost {cost}")
      print(f"이전 : distance[i[0]] { distance[i[0]]}")

      #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
          distance[i[0]] = cost
          heapq.heappush(q, (cost, i[0]))
      print(f"변경 : distance[i[0]] { distance[i[0]]}")

dijkstra(start)
print("@@@@@distance : ", distance)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
  # 도달할수없는 경우, 무한을 출력
  if distance[i] == INF:
    print("INFINITY")
  # 도달할 수 있는 경우 거리를 출력
  else:
    print(distance[i])

 '''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n + 1)]
print("graph : ", graph)
distance = [INF] * (n + 1)
print("distance : ", distance)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijsktra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijsktra(start)

for i in range(1, n + 1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])
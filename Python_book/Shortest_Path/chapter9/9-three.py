import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, start= map(int, input().split())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))


def dijkstra(start):
  q = []
  # 시작하는것의 거리는 0이기때문에 아래와 같이 heap을 시작
  heapq.heappush(q, (0,start))
  # distance의 거리는 0으로 만들어주어야함
  distance[start] = 0
  while q:
    # 큐에서 첫번째로 있는것을 pop
    dist, now = heapq.heappop(q)
    # 해당노드를 처리한적이있다면 무시
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distance)

count = 0
max_distance = 0
for d in distance:
  if d != INF:
    count += 1
    max_distance = max(max_distance, d)

print(count - 1, max_distance)

# for i in range(1, n + 1):
#   if distance[i] == INF:
#     print("INFTINITY")
#   else:
#     print(distance[i])
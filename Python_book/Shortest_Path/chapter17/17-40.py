import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().split())

graph = [[] * (n + 1) for in range(n + 1)]
distance = [INF] * (n + 1)

start = 1

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append((b, 1))
  graph[b].append((a, 1))

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

  distance[0] = 0
  second = max(distance)
  first = distance.index(second)
  third = distance.count(second)
  print(frist, second, third)

dijsktra(start)
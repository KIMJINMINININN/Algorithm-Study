# 최단경로

## 1. 다익스트라
``다익스트라를 사용하기 좋은조건은 스타트할 부분이 정해져있고, 해당하는 노드의 범위가 한정적이지 않고 매우 많을때 사용하기 좋다 ex) 1 <= N <= 100000``

우선순위큐를 사용하여서 코드를 짜기에는 조금 복잡하지만
시간을 훨씬 단축시켜서 시간제한에 걸리지 않게할수있다.

우선순위큐 : 우선순위가 가장 높은것을 꺼내게 되는 방법
우선순위 큐 라이브러리에 데이터의 묶음을 넣으면 첫번째 원소를 기준으로 우선순위를 설정하게된다.
우선순위큐는 최소힙, 최대힙으로 나뉘는데 
- 최소힙은 :  값이 낮은 데이터가 먼저 나오게되고
- 최대힙은 :  값이 높은 데이터가 먼저 나오게된다.

Python에서는 최소힙으로 우선순위큐가 사용되어진다.
최대힙으로 사용하기 위해서는 아래와 같이 사용하면된다.
```
import heapq

def heapsort(iterable):
  h = []
  result = []
  for value in interable:
    heapq.heappush(h, -value)
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
```

``다익스트라에 대해서는 책에 p.247에 잘나와있으니 다시한번 참고``

### 다익스트라의 핵심 코드
핵심을 이해해서 어느정도 외워 응용하는것이 좋을듯
```
# 그래프 만들어주기
graph = [[] for i in range(n + 1)]
# 거리를 나타낼 데이터
distance = [INF] * (n + 1)

# 각각의 데이터에 아래와같이 입력 graph[a] (b, c)
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

# 다익스트라 알고리즘 코드
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
# 1.graph에 현재 그래프의 사용되는 가격이나 비용 입력
# 2.distance에 전체를 INF로 만들어주기
# 3.첫번째 스타트 하는 부분을 초기화시키고 큐에 입력
# 4.heap에서 각값을 빼낸다음 노드의 값과 다음으로 이동했을때의 비용을 더함
# 5.그값을 distance와 비교하여서 작은값을 distance에 입력시켜주고
# 6.해당하는 부분을 큐에 추가시켜준다
# 7.작업 반복후 distance 데이터 확인
```

## 2. 플로이드 워셜
``플로이드를 사용하기 좋은조건은 모든지점에서 다른 모든 지점까지의 최단경로를 구할때와 노드의 범위가 한정적일때 사용하기 좋다 ex) 1 <= N <= 100``

플로이드 워셜 알고리즘은 2차원 리스트에 최단거리 정보를 저장한다는 특징이있다.
이 방법은 한마디로 전체의 모든경로를 하나씩 다 돌면서 비교하겠다는 알고리즘
### 플로이드 핵심 점화식
a에서 b로 가는 최소비용과 a에서 k를 거쳐서 B로 가는 비용을 비교하여서
더작은 값으로 갱신하겠다는 의미

```
Dab = min(Dab, Dak + Dkb)
```
핵심을 이해해서 어느정도 외우는게 좋을듯
### 플로이드 핵심 코드
```
# 다이제스트라와 같이 graph를 INF로 만들어주고
graph = [[INF] * (n + 1) for i in range(n + 1)]
# 2차원 리스트에 값을 각각 입력
for _ in range(m):
  a, b, c = map(int,input().split())
  if c < graph[a][b]:
    graph[a][b] = c
# 대각선으로 같은 값들은 모두 0으로 만들어준다.
for i in range(1, n + 1):
  for j in range(1, n + 1):
    if i == j:
      graph[i][j] = 0

# 플로이드 알고리즘 실행
for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      graph[i][j] = min(graph[i][j] , graph[i][k] + graph[k][j])
```
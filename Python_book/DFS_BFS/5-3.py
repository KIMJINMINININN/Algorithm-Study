n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

print("graph : ", graph)

def dfs(x, y):
  # 종료 시키기
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  # 현재 노드 방문 하지않았다면
  # 노드의 방문을 현재 graph[][] = 1 로써 나타내는중
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x - 1, y) # 왼쪽
    dfs(x, y- 1)  # 위쪽
    dfs(x + 1, y) # 오른쪽
    dfs(x, y + 1) # 아래쪽 확인
    return True
  return False

# 모든 노드에 대하여 음료수
result = 0
for i in range(n):
  print("i : ", i )
  for j in range(m):
    print("  j : ", j )
    
    # 현재 위치에서 DFS 수행
    if dfs(i, j) == True:
      print("True에요!!!")
      result += 1
    
print(result)
#유기농 배추는 맛잇낭?
test_case = int(input())
result_list = []

def dfs(x, y):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  if graph[y][x] == 1:
    graph[y][x] = 0
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False

[1,2,3,4,5], [678910], [1112131415]
for i in range(test_case):
  n , m , k = map(int,input().split())
  graph = [[0] * (n) for i in range(m)]
  # print("graph : ", graph)
  for _ in range(k):
    a, b = map(int,input().split())
    graph[b][a] = 1
    # print("graph[b][a] : ", graph[b][a])
    # print(f"a : {a} , b : {b}")

  result = 0
  for i in range(n):
    for j in range(m):
      if dfs(i, j) == True:
        result += 1 
  result_list.append(result)

if(len(result_list) > 0):
  for i in result_list:
    print(i)
else:
  print()
#유기농 배추는 맛잇낭?
test_case = int(input())
result_list = []

def dfs(x, y):
  if x <= -1 or x >= n or y <= -1 or y >= n:
    return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False

for i in range(test_case):
  # print("while_docount : ", while_docount)
  # print("test_case : ", test_case)
  n , m , k = map(int,input().split())
  # print(f" n : {n}, m : {m}, k : {k}")
  graph = [[0] * (n+1) for i in range(n+1)]
  # print("graph : ", graph)

  for _ in range(k):
    a, b = map(int,input().split())
    graph[a][b] = 1
    # print(f" a : {a}, b : {b}")

  # print("graph : ", graph)

  result = 0
  for i in range(n):
    for j in range(m):
      if dfs(i, j) == True:
        result += 1 

  result_list.append(result)
  # print("result_list : ", result_list)
if(len(result_list) > 0):
  for i in result_list:
    print(i)
else:
  print()
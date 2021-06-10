#단지번호 붙이기
n = int(input())

graph = []
# test = [[0,1,1,0,1,0,0], [0,1,1,0,1,0,1], [1,1,1,0,1,0,1], [0,0,0,0,1,1,1], [0,1,0,0,0,0,0], [0,1,1,1,1,1,0], [0,1,1,1,0,0,0]]

for i in range(n):
  graph.append(list(map(int,input())))

# print("graph", graph)
def dfs(x, y):
  if x <= -1 or x >= n or y <= -1 or y >= n:
    return False
  if graph[x][y] == 1:
    a_list[one_count] += 1
    graph[x][y] = 0
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False

a_list = [0]
result_cont = 0
one_count = 0
for i in range(n):
  for j in range(n):
    if dfs(i, j) == True:
      a_list.append(0)
      result_cont += 1
      one_count += 1
a_list.remove(0)
a_list.sort()
print(result_cont)
for i in a_list:
  print(i)
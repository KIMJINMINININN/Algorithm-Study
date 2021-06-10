# 5-7
''' 
graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print("graph" , graph) 
'''

# 5-8
''' 
def dfs(graph, value, visited):
  visited[value] = True

  for i in graph[value]:
    if not visited[i]:
      dfs(graph, i, visited)
  
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited) '''

# 5 -9
''' 
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True

  while queue:
    v = queue.popleft()
    print(v, end= ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9 

bfs(graph, 1, visited) 
'''

# def test(a):
#   if a > 0:
#     return False

# def test1(b):
#   # t = test(1)
#   # print(t)
#   test(1)
#   return True
#   if b > 0:
#     return True

# print(test1(5))

from collections import deque, defaultdict

n, m, v = map(int,input().split())
graph = defaultdict(set)
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)
print("graph : " , graph)

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited
  
print(BFS_with_adj_list(graph, v))

def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

print(BFS_with_adj_list(graph, v))
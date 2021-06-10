# # DFS와 BFS
# def dfs(graph, v, visitd):
#   visited[v] = True
#   print("v : ",v)
#   for i in graph[v]:
#     print("dfs i : ", i)
#     if not visited[i]:
#       dfs(graph, i , visited)

# # graph = [
# #   [],
# #   [2, 3, 8],
# #   [1, 7],
# #   [1, 4, 5],
# #   [3, 5],
# #   [3, 4],
# #   [7],
# #   [2, 6, 8],
# #   [1, 7]
# # ]

# n, m, v = map(int,input().split(" "))
# print("n : ", n, "m : ", m, "v: ", v)
# temp_list = [
#   []
# ]
# for i in range(0, m):
#   temp_list.append(list(map(int,input().split(" "))))

# graph = [
#   [] for i in range(n)
# ]

# for (i, value_i) in enumerate(temp_list):
#   # print("i : ", i)
#   # print("value_i : ", value_i)
#   for (j, value_j) in enumerate(value_i):
#     # print("j : ", j)
#     # print("value_i[1] : ", value_i[1])
#     if(j == 0):
#       if(len(value_i) >= 2):
#         graph[value_i[0]].append(value_i[1])
#     # print("graph : ", graph)
# print("graph : ", graph)

# visited = [False] * (int(len(graph)) + 1)
# print("visited : ", visited)
# dfs(graph, v, visited)
#------------------------------------------------
''' 
from collections import deque, defaultdict
# 들어온것을 dict으로 만들어주는 작업
n, m, v = map(int,input().split())
graph = defaultdict(set)
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)
print("graph : " , graph)

def dfs(v:int,graph:dict)->str:
    ret = ' '
    visited = []
    stack = [v]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += sorted(graph[n] - set(visited),reverse=True)
    ret = ret.join(str(i) for i in visited)
    return ret

def bfs(v:int,graph:dict)->str:
    ret = ' '

    visited = []
    queue = deque([v])

    while queue:
        print(f"queue: {queue} visited : {visited}")
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += sorted(graph[n] - set(visited))

    ret = ret.join(str(i) for i in visited)
    return ret

print(dfs(v,graph))
print(bfs(v,graph)) 
'''
#------------------------------------------------
''' 
# 이중 리스트로 만들어주는 작업
n, m, v = map(int, input().split())
s = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1

def dfs(v):
    print("v : ",v)
    visit[v] = 1
    for i in range(1, n + 1):
      if visit[i] == 0 and s[v][i] == 1:
          dfs(i)

def bfs(v):
    queue = [v]
    visit[v] = 0
    while(queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n + 1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0

dfs(v)
print()
bfs(v)
 '''
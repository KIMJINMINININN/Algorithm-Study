# 바이러스

from collections import deque, defaultdict
m = int(input()) # 노드수
n = int(input()) # 간선수
print("m :", m)

node_list = defaultdict(set)
for _ in range(n):
  a, b = map(int,input().split())
  node_list[a].add(b)
  node_list[b].add(a)

print("node_list :", node_list)

def dfs(v, node_list):
    ret = ' '
    visited = []
    stack = [v]
    while stack:
        n = stack.pop() # 맨위에 팝
        print("node_list[n] :", node_list[n])
        if n not in visited: # 방문했던게 아니라면
            print("n : ", n)
            visited.append(n) # 
            stack += sorted(node_list[n] - set(visited),reverse=True)
    visited.remove(1)
    ret = len(visited)
    # ret = ret.join(str(i) for i in visited)
    return ret

print(dfs(1,node_list))

# def bfs(v, node_list):
#     ret = ' '

#     visited = []
#     queue = deque([v])

#     while queue:
#         print(f"queue: {queue} visited : {visited}")
#         n = queue.popleft()
#         if n not in visited:
#             visited.append(n)
#             queue += sorted(node_list[n] - set(visited))

#     visited.remove(1)
#     ret = len(visited)
#     # ret = ret.join(str(i) for i in visited)
#     return ret

# print(bfs(1,node_list))
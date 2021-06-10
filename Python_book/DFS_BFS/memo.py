#memo 
# 1. list 입력 받는 방법
# 첫번째 입력 받기
# 101011
# 111111
# 111100
# 001110
''' 
n, m = map(int,input().split())
print(n , m)
graph = []
for i in range(n):
  graph.append(list(map(int, input())))
print("graph : ", graph) 
'''

# 두번재 입력 받기
# 5 3 6
# 0 2
# 1 2
# 2 2
# 3 2
# 4 2
# 4 0

''' 
n, m, k = list(map(int,input().split()))
print(n, m ,k)

graph = [[0] * (m) for i in range(n)]
print("graph : ", graph)

for _ in range(k):
  a, b = map(int,input().split())
  graph[a][b] = 1

print("graph : ", graph) 
'''
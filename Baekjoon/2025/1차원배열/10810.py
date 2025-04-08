import sys

n, m = map(int,sys.stdin.readline().split())

basket = [0 for i in range(n)]

for i in range(0, m):
    i, j, k = map(int,sys.stdin.readline().split())
    for j in range(i-1, j):
        basket[j] = k

for i in basket:
    print(i, end=" ")
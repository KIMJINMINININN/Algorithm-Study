import sys

n, m = map(int,sys.stdin.readline().split())

basket = [0 for i in range(n)]
for idx, val in enumerate(basket):
    basket[idx] = idx + 1


for t in range(0, m):
    i, j = map(int, sys.stdin.readline().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for i in basket:
    print(i, end=" ")
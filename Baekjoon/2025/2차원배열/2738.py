n, m = map(int,input().split())
a = []
b = []

for i in range(n):
    temp = list(map(int, input().split()))
    a.append(temp)

for i in range(n):
    temp = list(map(int, input().split()))
    b.append(temp)

result = [[0 for i in range(m)] for b in range(n)]

for i in range(len(a)):

    for j in range(len(a[i])):
        result[i][j] = a[i][j] + b[i][j]

        print(result[i][j], end=" ")

    print("")





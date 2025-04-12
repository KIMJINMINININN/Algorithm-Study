import sys

a, b = sys.stdin.readline().strip().split()

temp1 = [0 for i in range(len(a))]
temp2 = [0 for i in range(len(b))]

for i in range(len(a) - 1, -1, -1):
    temp1[len(a) -1 - i] = a[i]

for i in range(len(b) - 1, -1, -1):
    temp2[len(b) -1 - i] = b[i]

result1 = "".join(temp1)
result2 = "".join(temp2)

if result1 > result2:
    print(result1)
else:
    print(result2)
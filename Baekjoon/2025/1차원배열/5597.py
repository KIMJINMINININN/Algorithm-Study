import sys

num = [0 for i in range(30)]

for i in range(28):
    n = int(sys.stdin.readline())
    num[n - 1] = n

for idx, val in enumerate(num):
    if val == 0:
        print(idx + 1)
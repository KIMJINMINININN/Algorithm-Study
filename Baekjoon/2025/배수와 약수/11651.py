n = int(input())
nums = []

for i in range(0, n):
    x, y = map(int, input().split())
    nums.append((x, y))

nums.sort(key=lambda x: (x[1], x[0]))

for j in nums:
    print(j[0], j[1])

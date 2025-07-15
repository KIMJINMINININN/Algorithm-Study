n = int(input())
nums = []

for i in range(0, n):
    x, y = map(int, input().split())
    nums.append((x, y))

nums.sort()

for j in nums:
    print(j[0], j[1])

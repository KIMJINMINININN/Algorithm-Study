
# n, m = list(map(int,input().split()))
# money_list = []

# for _ in range(n):
#   money_list.append(int(input()))

# d = [0] * 10001

# for i in range(m):
  
#   print("di : ", d[i])
# print(n, m)
# print(money_list)


n , m = map(int, input().split())
array = []
for i in range(n):
  array.append(int(input()))

d = [10001] * (m + 1)
print(f"array : {array}")
d[0] = 0
for i in range(n):
  for j in range(array[i], m + 1):
    # print(f" j : {j}")
    # print(f"array[i] : {array[i]}")
    # print(f"before d[j] : {d[j]}")
    if d[j - array[i]] != 10001:
      d[j] = min(d[j], d[j - array[i]] + 1)
    # print(f"after d[j] : {d[j]}")
if d[m] == 10001:
  print(-1)
else:
  print(d[m])

d[j] = min(d[j], d[j - array[i]] + 1)

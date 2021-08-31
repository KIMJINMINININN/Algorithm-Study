# x = int(input())
# cout = 0
# a = [5, 3, 2]
# def function(num, x, cout):
#   if x % num == 0:
#     x = x / num
#     cout = cout + 1
#   return x, cout

# while x != 1:
#   for i in a:
#     x, cout = function(i, x, cout)
#   x = x - 1
# print(cout)

x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
  print(f"before d[{i}] : {d[i]}, d[{i - 1}] : {d[i - 1]}")
  d[i] = d[i - 1] + 1
  print(f"after d[{i}] : {d[i]}")
  if i % 2 == 0:
    # print("d[i // 2] + 1 : ", d[i // 2] + 1)
    d[i] = min(d[i], d[i // 2] + 1)
  if i % 3 == 0:
    # print("d[i // 3] + 1 : ", d[i // 3] + 1)
    d[i] = min(d[i], d[i // 3] + 1)
  if i % 5 == 0:
    # print("d[i // 5] + 1 : ", d[i // 5] + 1)
    d[i] = min(d[i], d[i // 5] + 1)
  print(f"min d[{i}] : {d[i]}")
print(d[x])
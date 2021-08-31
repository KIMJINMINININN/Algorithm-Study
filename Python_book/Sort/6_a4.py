n, k = input("").split(" ")
a = list(map(int, input("").split(" ")))
b = list(map(int, input("").split(" ")))

for i in range(int(k)):
  a = sorted(a)
  b = sorted(b, reverse = True)
  a_min = a[0]
  b_max = b[0]
  a[0] = b_max
  b[0] = a_min

print(sum(a))
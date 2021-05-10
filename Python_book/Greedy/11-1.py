# 겁쟁이
n = int(input(""))
x_list = list(map(int,input("").split(" ")))

x_list = sorted(x_list)
group = 0
sum_value = 0

for i in x_list:
  sum_value += 1
  if sum_value >= i:
    group += 1
    sum_value = 0

print(group)
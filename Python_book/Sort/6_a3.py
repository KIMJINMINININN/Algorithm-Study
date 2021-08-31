n = int(input(""))

temp_list = []
for i in range(n):
  name, value = input("").split(" ")
  temp_list.append((name, int(value)))

temp_list = sorted(temp_list, key=lambda student: student[1])

for i in temp_list:
  print(i[0], end=' ')
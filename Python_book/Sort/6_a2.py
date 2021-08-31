n = int(input(""))
temp_list = []
for i in range(n):
  temp_list.append(int(input("")))

# print("@@@temp_list : ", temp_list)
temp_list = sorted(temp_list, reverse = True)
for i in temp_list:
  print(i, end=' ')
# print("@@@temp_list : ", temp_list)
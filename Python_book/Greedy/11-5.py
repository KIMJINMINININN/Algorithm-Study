# 볼링공
# n, m = input("").split(" ")
# in_list = list(map(int,input("").split(" ")))

n = 8
m = 5
# in_list = [1, 2, 3, 4, 5]
in_list = [1, 5, 4, 3, 2 ,4, 5, 2]
my_dic = {}
value_count = 0
# print("n : ", n)
# print("m : ", m)
# print("in_list : ", in_list)

for count, value in enumerate(in_list):
  my_dic[count+1] = value

print(my_dic)
for i in my_dic:
  for j in range(i+1, len(my_dic)+1):
    if(i != j):
      if(my_dic[i] != my_dic[j]):
        value_count = value_count + 1
print("value_count : ", value_count )
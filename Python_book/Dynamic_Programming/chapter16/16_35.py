''' #못생긴수
n = int(input())

fault_number = [1]

n = 1
# while len(fault_number) == 1000:
while len(fault_number) != 1000:
  n = n + 1
  # print("n : ", n)
  for i in (2,3,5,6,10,15,30):
    temp = n
    temp = temp % i
    # print("  temp : ", temp)
    if temp == 0:
      fault_number.append(n)
      break

print(fault_number)
# print(fault_number[n])
 '''
''' n = int(input())
real_list = []
v = 1
while len(real_list) != 10:
  v = v + 1
  my_list = []
  i = 2
  while v != 1:
    if v%i == 0:
      v = v/i
      my_list.append(i)
    else:
      i += 1
  print("my_list : ", my_list)
  if 2 in my_list and 3 in my_list and 5 in my_list:
    print("test")
    real_list.append()
print("real_list : ", real_list) '''

n = int(input())

ugly = [0] * n
ugly[0] = 1

# 2, 3, 5배
i2 = i3 = i5 = 0
# 곱셈 초기화
next2, next3, next5 = 2, 3, 5

# 1부터 n까지 못생긴수 찾기
for l in range(1, n):
  ugly[l] = min(next2, next3, next5)
  if ugly[l] == next2:
    i2 += 1
    next2 = ugly[i2] * 2
  if ugly[l] == next3:
    i3 += 1
    next3 = ugly[i3] * 3
  if ugly[l] == next5:
    i5 += 1
    next5 = ugly[i5] * 5
  print(next2, next3, next5)
print(ugly[n - 1])
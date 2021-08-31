import sys
# rstrip()은 공백 문자를 제거하기위함
n = int(input())

food_list = list(map(int,sys.stdin.readline().rstrip().split(' ')))

print("food_list : ", food_list)
sum_x = 0
sum_y = 0 
# 홀수 합 구하기
for i in range(0, len(food_list), 2):
  sum_x = sum_x + food_list[i]
# print(sum_x)
# 짝수 합 구하기
for i in range(1, len(food_list), 2):
  sum_y = sum_y + food_list[i]
# print(sum_y)
# 홀수 짝수 합 비교해서 큰것
max_sum = max(sum_x, sum_y)
print(max_sum)

# ---------------------------
import sys
# rstrip()은 공백 문자를 제거하기위함
n = int(input())

food_list = list(map(int,sys.stdin.readline().rstrip().split(' ')))

# DP 테이블 초기화
d = [0] * 100

d[0] = food_list[0]
d[1] = max(food_list[0], food_list[1])
for i in range(2, n):
  d[i] = max(d[i - 1], d[i - 2] + food_list[i])

print(d[n - 1])


import sys
# rstrip()은 공백 문자를 제거하기위함
n = int(input())

food_list = list(map(int,sys.stdin.readline().rstrip().split(' ')))

d = [0] * 100

d[0] = food_list[0]
d[1] = max(food_list[0], food_list[1])
for i in range(2, n):
  d[i] = max(d[i -1], d[i - 2] + food_list[i])

d = [0] * 100

d[0] = food_list[0]
d[1] = max(food_list[0], food_list[1]
for i in range(2, n):
  d[i] = max(d[i - 1], d[i - 2] + food_list[i])

d = [0] * 100

d[0] = food_list[0]
d[1] = max(food_list[0], food_list[1])
for i in range(2, n):
  d[i] = max(d[i - 1], d[i - 2] + food_list[i])

d = [0] * 100

d[0] = food_list[0]
d[1] = max(food_list[0], food_list[1])

for i in range(2, n):
  d[i] = max(d[i - 1], d[i - 2] + food_list[i])

d = [0] * 100

# 첫번째 값넣고, 두번째에는 큰값을 비교해서 넣기, 이것이 홀수짝수 비교
d[0] = food_list[0]
d[1] = max(food_list[0], food_list[1])

for i in range(2, n):
  d[i] = max(d[i - 1], d[i - 2] + array[i])

d = [0] * 100

d[0] = food_list[0]
d[1] = max(food_list[0], food_list[1])

for i in range(2, n):
  d[i] = max(d[i - 1], d[i - 2] + food_list[i])
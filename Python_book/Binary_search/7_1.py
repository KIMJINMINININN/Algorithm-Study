# 이진탐색

import sys

n = int(input())
store_data = list(map(int,sys.stdin.readline().rstrip().split()))

m = int(input())
custom_data = list(map(int,sys.stdin.readline().rstrip().split()))

result = []

# print(f"n : {n}, store_data : {store_data}")
# print(f"m : {m}, custom_data : {custom_data}")

def check_list(store_data,target,start,end):
  while start <= end:
    mid = (start + end) // 2
    # print("end", end)
    if store_data[mid] == target:
      # print("yes")
      return 'yes'
    elif store_data[mid] > target:
      # check_list(store_data,target,start,mid - 1):
      # print("elif")
      end = mid - 1
    else:
      # check_list(store_data,target,mid + 1, end):
      # print("mid + 1")
      start = mid + 1
  return 'no'

store_data = sorted(store_data)
for i in range(len(custom_data)):
  result.append(check_list(store_data, custom_data[i], 0, n - 1))
  print(result)


# 계수 정렬
''' n = int(input())
array = [0] * 1000001

for i in input().split():
  array[int(i)] = 1

prit(array)

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
      print('yes', end=' ')
    else:
      print('no', end=' ') '''

#집합 자료형
'''
 n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

print(f"n : {n}, array : {array}")
print(f"m : {m}, x : {x}")

for i in x:
  if i in array:
    print('yes', end=' ')
  else:
    print('no', end=' ') 
'''
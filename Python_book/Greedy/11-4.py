''' 
# 만들수 없는 금액
# n = int(input(""))
# won_list = list(map(int,input("").split(" ")))
n = 8
won_list = [2,3,4,5,6,7,1,2]
# n = 5
# won_list = [3, 2, 1, 1, 9]
a_list = []
b_list = []
c_list = []
won_list.sort()
print("won_list : ", won_list)
value = 0

for first in range(0, len(won_list)):
  sum_thing = 0
  sum_thing = won_list[first]
  print("sum_thing : ", sum_thing)
  b_list.append(sum_thing)
  for second in range(0, len(won_list)):
    if(first != second):
      sum_thing += won_list[second]
      b_list.append(sum_thing)
    else:
      pass
  a_list.append(b_list)
  b_list = []

print("a_list : ", a_list)
answer = list(set(sum(a_list, [])))
n = 1
for i in answer:
  if(n == i):
    n = n + 1
  else:
    print(n)
    break 
    '''

n = int(input())
data = list(map(int, input().split()))
data.sort()
print("data : ", data)
target = 1
for x in data:
  print("x : ", x)
  print("target : ", target)
  if target < x:
    break;
  target += x

print(target)
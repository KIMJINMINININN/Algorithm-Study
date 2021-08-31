import sys
from bisect import bisect_left, bisect_right

# -15 -4 2 8 13
n = int(input())
a_list = list(map(int,sys.stdin.readline().rstrip().split(' ')))
a_list.sort()

print("a_list : ", a_list)

def test(value, start, end):
  while True:
    if start > end:
      return 'no'
  # for i in range(3):
    mid = (end + start) // 2
    # print("mid : ", mid)
    # print("a_list[mid] : ", a_list[mid])
    if a_list[mid] == mid :
      return mid
    elif a_list[mid] < mid:
      start = mid + 1
    else:
      end = mid - 1
    # print("start : ", start)
    # print("end : ", end)

t = test(a_list, 0, len(a_list)-1)
if t == 'no':
  print("-1")
else:
  print(t) 

# i_bool = bisect_left(a_list , i)
# if n_bool == i:
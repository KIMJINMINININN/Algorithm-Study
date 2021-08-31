import sys
from bisect import bisect_left, bisect_right

def two_list(my_list, target):
  # while start <= end:
  b = bisect_left(my_list, m)
  c = bisect_right(my_list, m)
  count = c - b
  return count

# n : 갯수   m : 길이
n, m = list(map(int,input().split()))

my_list = list(map(int,sys.stdin.readline().split()))
my_list.sort()

result = two_list(my_list, m)
if count == 0:
  print('-1')
else:
  print(result)
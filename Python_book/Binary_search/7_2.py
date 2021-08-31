import sys

def two_list(my_list, start, end, result):
  while start <= end:
    sum_tuck = 0
    mid = (start + end) // 2
    print("mid : ", mid)
    for i in my_list:
      print("i : ", i)
      if i > mid:
        sum_tuck = sum_tuck + (i - mid)
    if sum_tuck < m:
      end = mid - 1
    else:
      result = mid
      start = mid + 1
  return result

# n : 갯수   m : 길이
n, m = list(map(int,input().split()))

my_list = list(map(int,sys.stdin.readline().split()))
my_list.sort()

result = 0
result = two_list(my_list, 0, my_list[len(my_list) - 1], result)
print(result)

'''
from sys import stdin

N, M = map(int,stdin.readline().split())

array = list(map(int,stdin.readline().split()))

def main(M:int,array:list,start:int,end:int)->int:
    ret = 0

    while end >= start:
        print(f"start : {start}, end : {end}")
        mid = (start+end) // 2
        tmp_array = [i for i in array if i > mid]
        tmp_res = sum(tmp_array) - len(tmp_array) * mid
        
        if tmp_res == M:
            ret = mid
            break
        elif tmp_res > M:
            start = mid+1
            ret = max(ret,mid)
        elif tmp_res < M:
            end = mid-1

    return ret

print(main(M,array,0,max(array)))

'''
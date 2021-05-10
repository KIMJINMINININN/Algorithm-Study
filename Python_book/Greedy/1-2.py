# n: list 갯수 m: 더하는 횟수 k: 한 index의 더하는 제한수
n, m, k = map(int,input('').split())
a_list = input('').split()
sum = 0
a_list = list(map(int, a_list))
a_list.sort()
if(a_list[-1] == a_list[-2]):
  for i in range(m):
    sum += a_list[-1]
else:
  while(m != 0):
    for i in range(k):
      if(m == 0):
        break
      else:
        sum += a_list[-1]
        m = m - 1
    if(m != 0):
      sum = sum + a_list[-2]
      m = m - 1
print(sum)
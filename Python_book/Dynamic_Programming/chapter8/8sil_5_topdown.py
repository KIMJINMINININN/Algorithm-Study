''' 
n, m = list(map(int,input().split()))
money_list = []

d = [10001] * (m + 1)

for _ in range(n):
  money_list.append(int(input()))

def find(a):
  if a < 0 : return 10001
  cal = 10001
  if d[a] != 0 : return d[a]
  for i in money_list:
    if find(a - i) < cal:
      cal = find(a - i)
  d[a] = cal + 1
  return d[a]

print(find(m) if find(m) < 10001 else -1) 
'''
# 오전 5_1, 1, 2
# 오후 3, 4, 5
# 집 6

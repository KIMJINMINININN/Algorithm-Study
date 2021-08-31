n = int(input())
# d = [0] * 1000001
d = [0] * 30001

def top_down(n):
  if n == 1: return 0;
  if(d[n] != 0): return d[n]
  
  d[n] = top_down(n - 1) + 1

  if n % 2 == 0:
    temp = top_down(int(n / 2)) + 1
    d[n] = min(d[n], temp)
  
  if n % 3 == 0:
    temp = top_down(int(n / 3)) + 1
    d[n] = min(d[n], temp)
  
  if n % 5 == 0:
    temp = top_down(int(n / 5)) + 1
    d[n] = min(d[n], temp)
  
  return d[n]

print(top_down(n))


import time

n = int(input())
p_temp = str(input())

start_time = time.time()
p_temp = str.split(p_temp)
sum_all = 0

p = list( map(int , p_temp) )
p.sort()
for i in range(n):
  tar = sum(p[0:i+1])
  sum_all += int(tar)
print(sum_all)
end_time = time.time()
print("time : ", end_time - start_time)


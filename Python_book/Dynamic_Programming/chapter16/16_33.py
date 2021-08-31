''' n = int(input())
dp = [[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]
# dp = []
# for _ in range(n):
#   dp.append(list(map(int,input().split())))

print("dp : ", dp)

for i in range(n):
  print(dp[i])
  # 날짜의 값이 n값을 넘지 않는다면! 더해볼수잇다.
  # 날짜의 값안에 있는것들 한번씩 다해서 다른것이 최대값이 잇는지 확인
  max_value = 0
  timer = dp[i][0]
  # for j in range(timer):
    # dp[i + j]
  # if i + dp[i][0]  > n
  #   pass
 '''
################################################
n = int(input()) 
t = [] #각 상담을 완료하는데 걸리는 기간
# t = [3, 5, 1, 1, 2, 4, 2]
p = [] #각 상담을 완료했을때 받을수 있는 금액
# p = [10, 20, 10, 20, 15, 40, 200]

dp = [0] * (n + 1) #dp 초기화
max_value = 0

for _ in range(n):
  x, y = map(int, input().split())
  t.append(x)
  p.append(y)
# print(f" t : {t} , p : {p} ")

for i in range(n - 1, -1, -1):
  # print("i : ", i)
  time = t[i] + i
  # 시간안에 인것이라면
  if time <= n:
    # print(" p[i] : ", p[i] )
    # print(" dp[time] : ", dp[time])
    dp[i] = max(p[i] + dp[time], max_value)
    max_value = dp[i]
    # print(" max_value : ", max_value)
    # print(" dp : ", dp)
  # 시간안에 것이 아니라면
  else:
    dp[i] = max_value

print(max_value)
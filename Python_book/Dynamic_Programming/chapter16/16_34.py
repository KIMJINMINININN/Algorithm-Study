''' n = int(input())

solider = list(map(int,input().split()))
dp = [0] * n
print("solider : ", solider)
print("dp : ", dp)
for i in range(n):
  if i == 0:
    if solider[i] > solider[i + 1]:
      dp[i] = 0
    else:
      dp[i] = 1
  elif i == n - 1:
    if solider[i - 1] > solider[i]:
      dp[i] = 0
    else:
      dp[i] = 1
  else:
    if solider[i - 1] > solider[i] > solider[i + 1]:
      dp[i] = 0
    else:
      dp[i] = 1

count = 0
for i in dp:
  if i == 1:
    count = count + 1

print(int(count / 2))
# solider = sorted(solider, reverse=True)

# print("solider : ", solider) '''

#----------------------------------------------------------#
# 가장 긴 증가하는 부분 수열 사용 (LIS) Youtube 들어보기
n = int(input())

array = list(map(int, input().split()))

array.reverse();

print("array : ", array)
dp = [1] * n

for i in range(1, n):
  print("array[i] : ", array[i])
  for j in range(0, i):
    # 작은것이 잇다면
    if array[j] < array[i]:
      print("    array[j] : ", array[j])
      print("    dp : ", dp)
      print("    dp[i] : ", dp[i])
      print("    dp[j] : ", dp[j])
      dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
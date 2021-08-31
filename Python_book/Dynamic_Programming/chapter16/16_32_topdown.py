n = int(input())
# dp = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
dp = []
for _ in range(n):
  dp.append(list(map(int,input().split(' '))))

print(dp)

for i in range(1, n):
  for j in range(len(dp[i])):
    if i == 
    # print("   j : ", j)
    #j - 1 < 0일때 (오른쪽것만 더한다)
    if (j - 1 < 0) :
      dp[i][j] = dp[i][j] + dp[i - 1][j]
    #j - 1 >= 0일때 (왼쪽 오른쪽의 max값을 더한다)
    elif j - 1 >= 0 and j < len(dp[i]) - 1:
      # print("1 elif")
      dp[i][j] = dp[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])
    #j + 1 >= len(dp[i]) - 1일때 (왼쪽값만 더한다)
    elif j + 1 >= len(dp[i]) - 1:
      # print("2 elif")
      dp[i][j] = dp[i][j] + dp[i - 1][j - 1]
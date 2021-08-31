# t = int(input())

n, m = list(map(int, input().split()))

gang = list(map(int, input().split()))
dp = []
for i in range(n):
  dp.append(gang[(m*i):(m*(i+1))])

print(dp)

def solution(i, j):
  # 왼쪽 위에서 오는 경우
  if i == 0:
    print("왼쪽위 if")
    left_up = 0
  else:
    print("왼쪽위 else")
    left_up = solution(i - 1,j - 1)
  # 왼쪽 아래에서 오는경우
  if i == n - 1:
    print("왼쪽아래 if")
    left_down = 0
  else:
    print("왼쪽아래 else")
    left_down = solution(i + 1,j - 1)
  # 왼쪽에서 오는경우
  left = solution(i,j - 1)
  dp[i][j] = dp[i][j] + max(left_up, left_down, left)
  return dp[i][j]


solution(n, m)
print(dp)
result = 0

for i in range(n):
  result = max(result, dp[i][m - 1])

print(result)
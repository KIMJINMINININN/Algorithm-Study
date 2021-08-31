import sys
sys.setrecursionlimit(5000)

n = int(input())

dp = [0] * 101
food_list = list(map(int, input().split()))

print('food_list : ', food_list)

dp[0] = food_list[0]
dp[1] = max(food_list[0] , food_list[1])

def solution(n):
  dp[n] = max(solution(n - 1), solution(n - 2) + food_list[n])

  return dp[n]

print(solution(n))
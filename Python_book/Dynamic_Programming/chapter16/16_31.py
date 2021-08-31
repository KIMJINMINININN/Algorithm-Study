import sys

t = int(input())
for i in range(t):
  real_list = []
  n , m = list(map(int,input().split()))

  gold_list = [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]
  # gold_list = list(map(int,sys.stdin.readline().rstrip().split(' ')))  
  # print('gold_list : ', gold_list)

  # 이중 리스트로 만들어주기
  a = m
  for i in range(n):
    if m == 0:
      real_list.append(gold_list[:a])
    else:
      real_list.append(gold_list[a-m:a])
    a = a + m

  print("@@@@@ real_list : ", real_list)

# j가 1부터 시작하는이유는, 0은 그대로 놔두어도 되서
  for j in range(1, m):
    print("j : ", j)
    for i in range(n):
      # 왼쪽 위에서 오는 경우
      print("   i : ", i)
      if i == 0:
        print("왼쪽위 if")
        left_up = 0
      else:
        print("왼쪽위 else")
        left_up = real_list[i - 1][j - 1]
      # 왼쪽 아래에서 오는경우
      if i == n - 1:
        print("왼쪽아래 if")
        left_down = 0
      else:
        print("왼쪽아래 else")
        left_down = real_list[i + 1][j - 1]
      # 왼쪽에서 오는경우
      left = real_list[i][j - 1]
      real_list[i][j] = real_list[i][j] + max(left_up, left_down, left)

  print(real_list)
  result = 0

  for i in range(n):
    result = max(result, real_list[i][m - 1])

  print(result)  
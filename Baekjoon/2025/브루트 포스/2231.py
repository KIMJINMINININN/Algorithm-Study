# 어떤 자연수 N
# 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
# 자연수 M의 분해합이 N인경우, M을 N의 생성자라 한다.
# 245의 분해합 = 256(245 + 2 + 4 + 5).
# 245는 256의 생성자가 된다.
# 자연수 N이 주어졌을때 가장 작은 생성자를 구하는 프로그램을 작성하라.

import sys
input = sys.stdin.readline

# 입력
n = int(input())

for i in range(n):
    # 분해합 공식
    digit_sum = i + sum(map(int, str(i)))
    # 생성자일 경우
    if digit_sum == n:
        print(i)
        break
else:
    print(0)
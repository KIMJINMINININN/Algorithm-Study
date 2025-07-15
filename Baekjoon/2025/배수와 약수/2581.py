import math

def is_prime_number(x):
    # 1 이하는 소수가 아님
    if x < 2:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

m = int(input())
n = int(input())

sum = 0
min = 0

for i in range(m, n + 1):
    if is_prime_number(i):
        sum += i
        if min == 0:
            min = i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)
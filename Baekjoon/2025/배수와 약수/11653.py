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

def is_prime_number_to(x):
    # 1 이하는 소수가 아님
    if x < 2:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return i # 소수가 아님
    return 0 # 소수임

n = int(input())

while(True):
    if n == 1:
        break

    if is_prime_number(n):
        print(int(n))
        break
    else:
        num = is_prime_number_to(n)
        print(int(num))
        if num == 0:
            break
        mox = n / num
        namergic = n % num
        n = int(mox)




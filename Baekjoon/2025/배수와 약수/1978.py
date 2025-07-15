n = int(input())
nums = list(map(int, input().split()))
prime_count = 0

for x in nums:
    if x < 2:
        continue  # 2 미만은 소수가 아님
    is_prime = True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_count += 1

print(prime_count)
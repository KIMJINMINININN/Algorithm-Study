a, b = map(int, input().split())

tmp = []
for i in range(1, min(a,b) + 1):
    if a % i == 0 and b % i == 0:
        tmp.append(i)

print(max(tmp))
print(max(tmp) * (a // max(tmp)) * (b // max(tmp)))

# a, b = map(int, input().split())
#
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a
#
# def lcm(a, b):
#     return a * b // gcd(a, b)
#
# print(gcd(a, b))
# print(lcm(a, b))
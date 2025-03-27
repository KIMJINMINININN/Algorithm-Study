a, b, c = map(int,input().split())

# 1번 같은 눈이 3개
if a == b and b == c:
    money = 10000+(a*1000)
    print(money)
# 2번 같은 눈이 2개
elif a == b or b == c or a == c:
    if a == b:
        money = 1000+(a*100)
        print(money)
    elif b == c:
        money = 1000+(b*100)
        print(money)
    elif a == c:
        money = 1000+(a*100)
        print(money)
# 3번 모두 다른 눈
elif a != b and a != c and b != c:
    numbers = [a, b, c]
    maximum = max(numbers)
    print(maximum * 100)

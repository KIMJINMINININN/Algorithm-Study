def commonFunction(a,b):
    while b >= 60:
        a = a + 1
        b = b - 60
        if a > 23:
            a = 0
    print(str(a) + " " + str(b))

a, b = map(int,input().split())
c = int(input())

b = b + c
if b > 60:
    commonFunction(a, b)
elif b == 60:
    commonFunction(a, b)
elif b < 60:
    print(str(a) + " " + str(b))

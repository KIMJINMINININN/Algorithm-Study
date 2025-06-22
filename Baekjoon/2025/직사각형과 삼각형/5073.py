# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error

# 단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다.
# 예를 들어 6, 3, 2가 이 경우에 해당한다.
# 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.

# 7 7 7
# 6 5 4
# 3 2 5
# 6 2 6
# 0 0 0

while(True):
    a, b, c = map(int,input().split())

    if a == 0 and b == 0 and c == 0:
        break

    maxValue = max([a, b, c])
    maxSecond = 0
    maxThrid = 0

    if maxValue == a:
        maxSecond = b
        maxThrid = c
    elif maxValue == b:
        maxSecond = a
        maxThrid = c
    elif maxValue == c:
        maxSecond = a
        maxThrid = b

    if maxValue >= (maxSecond + maxThrid):
        print("Invalid")
    elif a == b and a == c and b == c:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles")
    elif a != b and a != c and b != c :
        print("Scalene")


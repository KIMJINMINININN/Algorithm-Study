# 일반적인것
# import sys
# a = int(sys.stdin.readline())
#
# 정해진 갯수를 가지고 받을때
# import sys
# a, b, c = map(int, sys.stdin.readline().split())
#
# 임의의 갯수를 받을때
# import sys
# data = list(map(int, sys.stdin.readline().split()))

import sys
t = int(sys.stdin.readline())

for i in range(0, t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
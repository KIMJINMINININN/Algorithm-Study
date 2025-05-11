a, b, v = map(int, input().split())

if (v-b) % (a-b) == 0:
    print((v-b)//(a-b))
else:
    print((v-b)//(a-b)+1)

# while v > 0:
#     day += 1
#     # 낮
#     v = v - a
#     if v == 0:
#         break
#     # 밤
#     v = v + b
#
# print(day)

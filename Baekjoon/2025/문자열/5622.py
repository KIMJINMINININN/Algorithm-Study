# a = input()
# mySum = 0
#
# def test(text):
#     if "ABC".find(text) >= 0:
#         return 3
#     elif "DEF".find(text) >= 0:
#         return 4
#     elif "GHI".find(text) >= 0:
#         return 5
#     elif "JK".find(text) >= 0:
#         return 6
#     elif "MNO".find(text) >= 0:
#         return 7
#     elif "PQRS".find(text) >= 0:
#         return 8
#     elif "TUV".find(text) >= 0:
#         return 9
#     elif "WXYZ".find(text) >= 0:
#         return 10
#     else:
#         return 0
#
# for i in a:
#     mySum += test(i)
#
# print(mySum)


###------------------------------------------


dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)
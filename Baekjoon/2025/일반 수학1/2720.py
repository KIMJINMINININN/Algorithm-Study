t = int(input())
mylist = []
moneylist = [25, 10, 5, 1]

for i in range(t):
    mylist.append(int(input()))

for i in mylist:
    a = 0
    b = 0
    c = 0
    d = 0
    for index, moneny in enumerate(moneylist):

        if index == 0:
            a = i // moneny
            i = i % moneny
        elif index == 1:
            b = i // moneny
            i = i % moneny
        elif index == 2:
            c = i // moneny
            i = i % moneny
        elif index == 3:
            d = i // moneny
            i = i % moneny

    print(a, b, c, d)
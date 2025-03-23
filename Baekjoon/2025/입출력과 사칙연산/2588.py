first = str(input())
second = str(input())

plus = 0
for i in range(0, len(first)):
    plus += int(first) * int(second[len(second)-(1+i)]) * (10 ** i)
    print(int(first) * int(second[len(second)-(1+i)]))
print(plus)
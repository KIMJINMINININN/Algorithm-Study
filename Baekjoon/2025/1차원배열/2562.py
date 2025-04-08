numlist = []
for i in range(0, 9):
    n = int(input())
    numlist.append(n)

print(max(numlist))
print(numlist.index(max(numlist)) + 1)

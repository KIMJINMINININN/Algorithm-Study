n, k = map(int, input().split())

myList = []

for i in range(n):
    if n % (i+1) == 0:
        myList.append(i+1)

if len(myList) > k-1:
    print(myList[k-1])
else:
    print(0)

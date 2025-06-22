n, k = map(int, input().split())
myList = list(map(int, input().split()))

myList.sort(reverse=True)

print(myList[k-1])
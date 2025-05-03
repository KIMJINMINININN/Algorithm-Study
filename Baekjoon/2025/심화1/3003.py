orginalList = [1, 1, 2, 2, 2, 8]
chestList = list(map(int, input().split()))
myList = [0, 0, 0, 0, 0, 0]

for idx, val in enumerate(orginalList):
    if val == chestList[idx]:
        myList[idx] = 0
    else: ## chestList의 값이 작거나 클때
        myList[idx] = val - chestList[idx]

for i in myList:
    print(i, end=" ")
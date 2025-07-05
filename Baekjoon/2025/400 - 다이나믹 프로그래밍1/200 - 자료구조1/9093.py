n = int(input())

dictionList = []

for i in range(0, n):
    dictionList.append(list(map(str,input().split())))

for myList in dictionList:
    ## 한줄
    for index, item in enumerate(myList):
        itemStr = str(item)
        listItem = list(itemStr)
        listItem.reverse()
        listItem = "".join(listItem)
        myList[index] = listItem

    ## 한줄
    listItem = " ".join(myList)
    print(listItem)





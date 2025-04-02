a = int(input())
myList = []

for i in range(a):
    list1, list2 = map(int,input().split())
    myList.append([list1, list2])

for [first, last] in myList:
    print(first+last)


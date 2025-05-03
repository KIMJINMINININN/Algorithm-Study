n = int(input())

myList = []
num = 0
for i in range(n):
    text = input()
    myList.append(text)

for text in myList:
    obj = {}
    before = ""
    for i in text:
        # 이전에 값이 다른값이라면?
        if before != i:
            if i in obj:
                obj[i] += 1
                before = i
            else:
                obj[i] = 1
                before = i
    max = 0
    for i in obj.values():
        if i > 1:
            max = i

    if max == 0:
        num += 1

print(num)





n = int(input())
dicList = []

for i in range(0, n):
    num, name = map(str, input().split())
    dicList.append({"age": int(num), "name": name, "number": i})

dicList.sort(key=lambda x: x["number"])
dicList.sort(key=lambda x: x["age"])

for i in dicList:
    print(i["age"], i["name"])
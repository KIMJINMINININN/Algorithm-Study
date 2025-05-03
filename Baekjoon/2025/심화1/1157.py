chestList = input()

obj = {}

for text in chestList:
    if text.upper() in obj:
        obj[text.upper()] += 1
    else:
        obj[text.upper()] = 1

maxStr = ""
maxInt = 0
for key, value in obj.items():
    if value > maxInt:
        maxInt = value
        maxStr = key
    elif value == maxInt:
        maxInt = value
        maxStr = "?"

print(maxStr)
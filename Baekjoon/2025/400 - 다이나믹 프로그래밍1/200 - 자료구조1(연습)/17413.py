import sys
import re
input = sys.stdin.readline

s = input().rstrip()
# <로 시작하는경우
temp = re.findall(r'<[^>]+>|[^<]+', s)

a = []
for item in temp:
    if item[0].startswith('<'):
        a.append(item)
    else:
        itemSplit = item.split(" ")
        t = []

        for i in itemSplit:
            reItem = "".join(reversed(i))
            t.append(reItem)
        sorted_string_reversed = " ".join(t)
        a.append(sorted_string_reversed)
print(a)
sys.stdout.write("".join(a))
n, m = map(int, input().split())
mylist = []
min_list = []

for i in range(n):
    mylist.append(list(map(int, input().split())))

for a in mylist:
  min_list.append(min(a))
value = max(min_list)
print(value)

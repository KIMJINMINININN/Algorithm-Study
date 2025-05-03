import sys

num = int(sys.stdin.readline().strip())
mylist = []

for i in range(num):
    a, b = sys.stdin.readline().strip().split(" ")

    tmp = ""
    for j in b:
        for t in range(int(a)):
            tmp += j

    mylist.append(tmp)

for t in mylist:
    print(t)



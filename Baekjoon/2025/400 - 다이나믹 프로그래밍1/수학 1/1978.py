n = int(input())

mylist = list(map(int, input().split()))

# 소수: 수를 1과 자신을 제외하고 나눴을때 약수가 없는것
count = 0
for i in mylist:
    for j in range(2, i+1):
        if i % j == 0:
            if j == i:
                count += 1
            break
print(count)



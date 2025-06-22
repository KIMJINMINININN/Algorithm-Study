# n장의 카드를 숫자가 보이도록 놓는다.
# 딜러는 숫자 M을 크게 외친다.
# 3장의 카드를 골라야한다
# 블랙잭 변형이기에 합은 M을 넘지않고, M과 최댛나 가깝게 만들어야한다.
# M을 넘지않고, M에 최대한 가까운 카드 3장의 합.

n, m = map(int,input().split())
cardList = list(map(int,input().split()))

mySum = 0

for i in cardList:
    for j in cardList:
        for t in cardList:
            if i != j and i != t and j != t:
                # print("i : ", i)
                # print("j : ", j)
                # print("t : ", t)
                # print("=========")
                temp = i + j + t
                if temp <= m:
                    mySum = max(temp, mySum)

print(mySum)
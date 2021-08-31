a = int(input(''))
number_card = []
for _ in range(a):
  number_card.append(int(input('')))

print("number_card : ", number_card)
sum_list = []
number_card = sorted(number_card)
temp = 0
sum_all = 0
for i in range(len(number_card) - 1):
  if i == len(number_card) - 2:
    print("@@@ i: ", i)
    print("number_card[i] + number_card[i+1]", number_card[i] , number_card[i+1])
    temp =  temp + number_card[i+1]
    print("sum_list : ", sum_list)
    sum_all = sum(sum_list)
  else:
    print("### i:", i)
    temp = number_card[i] + number_card[i+1]
    sum_list.append(temp)
    print("sum_list : ", sum_list)

print("sum_all : ", sum_all)
  # if i == 0:
  #   
  #   if i + 2 > len(number_card):
  #     break
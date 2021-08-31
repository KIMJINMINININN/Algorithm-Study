# 안테나
## 시간초과 코드
''' 
n = int(input())

all_list = list(map(int, input("").split(" ")))

all_list = sorted(all_list)
# print("all_list :", all_list)
sum_list = {}
for (i, tmp_value) in enumerate(all_list):
  # print("tmp_value : ", tmp_value)
  tmp_sum = 0
  for (j, value) in enumerate(all_list):
    if i != j: # 1 != 1
      tmp_sum = tmp_sum + abs(tmp_value - value)
      # print("tmp_sum : ", tmp_sum)
  sum_list[tmp_value] = abs(tmp_sum)

def f1(x):
    return sum_list[x]

print("sum_list: ", sum_list)
key_min = min(sum_list.keys(), key=(lambda k: sum_list[k]))
print(key_min) '''


n = int(input())
data = list(map(int,input().split()))

data.sort()

print(data[(n-1)//2])


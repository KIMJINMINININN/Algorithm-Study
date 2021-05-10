# 주유소

# count = int(input(""))
# km = list(map(int,input("").split(" ")))
# price = list(map(int,input("").split(" ")))

# sum_price = 0
# n = 0
# low_index = 1

# if(count == 2):
#     sum_price = sum_price + (price[0] * km[0])
# else:
#   while(n <= count):
#     print("count : ", count)
#     if(price[n] == min(price[n:len(price)-1])): # yes
#       print("n : ", n )
#       print("yes!!!!")
#       sum_price = sum_price + (price[n] * sum(km[n:]))
#       break
#     else: #no
#       # 지금 걔보다 더 작은거가 어디에있는거야??
#       print("price[n:len(price)-1] : ", price[n:len(price)-1])
#       low_index = price.index(min(price[n:len(price)-1]))
#       print("low_index : ", low_index)
#       sum_price = sum_price + (price[n] * sum(km[n:low_index]))
#       print("price[n] : ", price[n])
#       print("sum(km[n:low_index]) : ", sum(km[n:low_index]))
#       print("sum_price : ", sum_price)
#       n = low_index - 1
#       n = n + 1
#       print("n : ", n)
# # [t:]이 최솟값인가?
# # 4
# # 1 1 1
# # 4 3 2 1
# # 답 9  
# print("sum_price : ", sum_price)
###################################################
n = int(input())
dists = list(map(int,input().split()))
costs = list(map(int,input().split()))

def main(n:int, dists:list, costs:list)->int:
  ## ret : 값, dists : 길이 , cost : 비용
    ret = 0
    
    ret += dists[0]*costs[0]
    base_cost = costs[0]
    base_dist = 0

    for idx in range(1,n-1):
      ## base가되는 비용이 idx의 비용보다 크다면
        if base_cost > costs[idx]:
            ret += base_dist*base_cost
            base_cost = costs[idx]
            base_dist = 0
      ## base_dist
        base_dist += dists[idx]
        if idx == n-2:
            ret += base_dist*base_cost

    return ret

print(main(n, dists, costs))
# (11047번) 동전 0 
import time
n, k = map(int, input().split())
won_list = []
count = 0
# won_list = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
# won_list를 입력받아서 list로 만들기
for i in range(n):
  won_list.append(input(""))
start = time.time()
won_list = list(map(int, won_list))
won_list.sort(reverse=True)
# print("won_list", won_list)
# won_list
# won_list만큼 반복
for won in won_list:
  # 받은값에서 won 빼고, count 올려주기(k가 won보다 크거나 같아야한다)))
  while( k >= won ):
    mux = k // won 
    k -= won * mux
    count += 1 * mux
    if( k == 0):
      break;
# end = time.time()
print(count)
# print(end-start)
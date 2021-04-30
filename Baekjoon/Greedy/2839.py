# 내가 푼것(용량이 너무크다^^;; and 비효율적)
n = int(input("설탕 무게를 입력하세요 : "))
orgin_n = n
count = 0
count_list = []
a_list = list(range(0,n+1,5))
b_list = list(range(0,n+1,3))
for a in a_list :
  n = orgin_n
  count = 0
  if(a == 0):
    orgin_a = n 
    count_temp = count
  else:
    count = count + (1 * int(a / 5))
    #n값 정리
    n = n - a
    #그때의 n값 저장
    orgin_a = n 
    count_temp = count
    if(n == 0):
      count_list.append(int(count))
      continue
  for b in b_list :
    count = count_temp
    n = orgin_a
    if(b == 0):
      x = 5
    else:
      count = count + (1 * int(b / 3))
      n = n - b
      if(n == 0):
        count_list.append(int(count))
if(len(count_list) == 0):
  count_list.append(-1)
print(min(count_list))

# 우현 풀이
''' 
n = int(input())

def box_count(n:int)->int:
    ret = 0

    while True:
        if n%5 == 0:
            ret += n//5
            break
        ret += 1
        n -= 3
        
        # Base Case
        if n < 0:
            ret = -1
            break

    return ret

print(box_count(n)) 
'''

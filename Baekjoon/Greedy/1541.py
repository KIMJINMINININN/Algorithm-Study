#식 입력받기
d=input()
#'-'기준으로 나누기
s=d.split('-')
#맨앞에 있는 원소를 값으로하는 변수 
#덩어리들 입력받을 리스트 초기화
num=[]
for i in s:
  k=i.split('+')
  cnt=0
  for j in k:
    cnt+=int(j)
  num.append(cnt)
#처음건 더해주기
result=num[0]    
#result에 덩어리 다 구했으니 다 빼주기 
for i in range(1,len(num)):
  result-=num[i]

print(result)
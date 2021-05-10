# 곱하기 혹은 더하기

s = input("연산자 입력 : ")

sum = int(s[0])

for i in range(1, len(s)):
  num = int(s[i])
  if num <= 1 or sum <= 1:
    sum += num
  else:
    sum = sum * int(s[i])

print(sum)
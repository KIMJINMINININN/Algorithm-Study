# 문자열 뒤집기
# 0, 1로 split같은걸 해서 따로 묶어서
# 각 묶음이 적은걸 뒤집는다.

s = str(input(""))
zero_list = [];
one_list = [];
print("s : ", s)
sum = ""
snap_count = 0
for i in range(0, len(s)):
  if(s[i] == "0"):
    if(sum.find("1") == 0):
      one_list.append(sum)
      sum = ""
    sum += "0"
  elif(s[i] == "1"):
    if(sum.find("0") == 0):
      zero_list.append(sum)
      sum = ""
    sum += "1"

if(sum.find("1") == 0):
  one_list.append(sum)
elif(sum.find("0") == 0):
  zero_list.append(sum)

if(len(zero_list) >= len(one_list)):
  snap_count = len(one_list)
else:
  snap_count = len(zero_list)

print("snap_count : ", snap_count)


''' 
# 해답풀이
data = input()
count0 = 0
count1 = 0

if data[0] == '1':
  count0 += 1
else:
  count1 += 1

for i in range(len(data) - 1):
  if data[i] != data[i+1]:
    if data[i + 1] == '1':
      count0 += 1
    else:
      count1 += 1

print(min(count0, count1))
'''
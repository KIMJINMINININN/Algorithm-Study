array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
  print("i : " , i)
  for j in range(i, 0 ,-1):
    if array[j] < array[j - 1]: # 앞에꺼가 뒤에꺼보다 크다면?
      array[j], array[j - 1] = array[j - 1], array[j]
    else: # 크지않으면 앞에꺼는 다 작은것이니 break
      print("@@@break")
      break
    print("array : ", array)

print(array)
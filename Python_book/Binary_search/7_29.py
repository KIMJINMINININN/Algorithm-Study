import sys

''' 
n, m = list(map(int,sys.stdin.readline().rstrip().split(" ")))
a_list = []
for i in range(n):
  a_list.append(int(sys.stdin.readline().rstrip()))

print(f"n : {n}, m : {m}")
print("a_list", a_list)

def two_road(all_list, start, end, middle):
  # while True:
  for _ in range(5):
    print(f" start : {start}, end  : {end} ")
    if start >= end:
      return
    print("while")
    mid = (start + end) // 2
    print("mid : ", mid)
    middle.append(mid)
    print("middle : ", middle)
    if start > end:
      return
    elif start < mid:
      start = mid + 1
    else:
      end = mid - 1


left_mid = []
right_mid = []
two_road(a_list, 0, (0 + n - 1) // 2, left_mid)
# two_road(a_list, left_mid[-1], n - 1, right_mid)

last_mid = left_mid + right_mid

last_mid.sort() '''


n, c = list(map(int,sys.stdin.readline().rstrip().split(" ")))
array = []

for _ in range(n):
  array.append(int(sys.stdin.readline().rstrip()))
array.sort()

start = array[1] - array[0] #집의 좌표중에 가장 작은 값
end = array[-1] - array[0] #집의 좌표중에 가장 큰값
result = 0

print(f"start : {start} , end : {end}")

while(start <= end):
  mid = (start + end) // 2
  value = array[0]
  count = 1
  # 현재의 mid 값을 이용해 공유기 설치
  for i in range(1, n): #앞에서 부터 차근차근 설치
    if array[i] >= value + mid:
      value = array[i]
      count += 1
  if count >= c: # C개 이상의 공유기를 설치할수있는 경우, 거리를 증가
    start = mid + 1
    result = mid # 최적의 결과를 저장
  else:
    end = mid - 1

print(result)
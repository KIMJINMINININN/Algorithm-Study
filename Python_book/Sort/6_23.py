# 1.국어 점수로 내림차순 ㅇ
# 2.국어 점수같다면 영어 점수 오름차순 
# 3.국어, 영어 같으면 수학점수 내림차순
# 4.모든조건이 같다면 이름 사전순으로 작성
# 국어 영어 수학

n = int(input())
a_list = []
for i in range(n):
    [Name, Kor, Eng, Math] = input().split()
    a_list.append([Name, Kor, Eng, Math])
print("a_list : ", a_list)
b_list = sorted(a_list, key= lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in range(n):
    print(b_list[i][0])
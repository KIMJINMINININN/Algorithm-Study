#L - 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
#D - 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
#B - 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
#삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
#P$	$라는 문자를 커서 왼쪽에 추가함

### 코드 시간초과
import sys
input = sys.stdin.readline

string = list(input().rstrip())
n = int(input())

cursor = len(string)

print(cursor)
for i in range(0, n):
    dic = input().rstrip()
    dicSplit = dic.split(" ")
    ## 텍스트 입력하는것
    if len(dicSplit) > 1:
        # print("cursor: ", cursor)
        p = dicSplit[0]
        text = dicSplit[1]
        string.insert(cursor, text)
        cursor = cursor + 1
    ## 커서 이동 및 삭제
    else:
        text = dicSplit[0]
        if text == "L":
            if cursor == 0:
                continue
            cursor = cursor - 1
        # D - 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
        elif text == "D":
            if cursor > len(string) + 1:
                continue
            cursor = cursor + 1
        # B - 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
        elif text == "B":
            if cursor == 0:
                continue
            del string[cursor - 1]
            cursor = cursor - 1
string = "".join(string)
print(string)
### 위의 코드 시간초과

### 답안

import sys
input = sys.stdin.readline

# 1) 초기 세팅
L = list(input().rstrip())
R = []
m = int(input())

# 2) 명령 처리
for _ in range(m):
    cmd = input().split()
    op = cmd[0]

    if op == 'L':
        if L:
            R.append(L.pop())

    elif op == 'D':
        if R:
            L.append(R.pop())

    elif op == 'B':
        if L:
            L.pop()

    elif op == 'P':
        # cmd == ['P', 'x']
        L.append(cmd[1])

# 3) 최종 문자열 출력
#    오른쪽 스택은 뒤집어서 붙이기
sys.stdout.write(''.join(L) + ''.join(reversed(R)))

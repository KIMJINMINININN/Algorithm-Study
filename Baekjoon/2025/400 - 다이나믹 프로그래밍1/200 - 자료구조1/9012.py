import sys
input = sys.stdin.readline
n = int(input())

output = []
for _ in range(n):
    s = input().rstrip()      # 개행 제거
    stack = []
    valid = True              # 올바른지 여부 플래그

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:  # ch == ')'
            if stack:
                stack.pop()  # 짝이 있으면 하나 꺼내고
            else:
                # 짝이 없으면 바로 잘못된 경우
                valid = False
                break

    # 반복이 끝난 뒤, valid하고 스택이 비어야만 올바름
    if valid and not stack:
        output.append("YES")
    else:
        output.append("NO")

print("\n".join(output))
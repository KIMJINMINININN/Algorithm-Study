n = int(input())
stack = []
output = []

for i in range(0, n):
    func = input()
    num = 0
    if "push" in func:
        a, b = func.split(" ")
        func = a
        num = b

    if func == "push" and num:
        stack.append(int(num))
    else:
        ## 각 명령어 대한 내용
        if func == "top":
            if len(stack) <= 0:
                output.append(-1)
                continue
            output.append(stack[len(stack) - 1])
        elif func == "pop":
            if len(stack) <= 0:
                output.append(-1)
                continue
            popNum = stack.pop()
            output.append(popNum)
        elif func == "size":
            output.append(len(stack))
        elif func == "empty":
            if len(stack) > 0:
                output.append(0)
            else:
                output.append(1)

for i in output:
    print(i)


# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
#
# 명령은 총 여섯 가지이다.
#
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
input = sys.stdin.readline

n = int(input())
queueList = []
output = []

for i in range(0, n):
    func = input().split()
    op = func[0]

    if op == "push":
        queueList.append(func[1])
    elif op == "pop":
        if len(queueList) == 0:
            output.append(-1)
            continue
        popText = queueList.pop(0)
        output.append(popText)
    elif op == "size":
        output.append(len(queueList))
    elif op == "empty":
        if len(queueList) == 0:
            output.append(1)
            continue
        else:
            output.append(0)
            continue
    elif op == "front":
        if len(queueList) == 0:
            output.append(-1)
            continue
        else:
            output.append(queueList[0])
            continue
    elif op == "back":
        if len(queueList) == 0:
            output.append(-1)
            continue
        else:
            output.append(queueList[len(queueList) - 1])
            continue

for i in output:
    print(i)



### 코드 시간초과
import sys
input = sys.stdin.readline

n = int(input())
myList = []
result = []

for i in range(0, n):
    ip = input().split()
    text = ip[0]
    # push_front X: 정수 X를 덱의 앞에 넣는다.
    if text == "push_front":
        num = ip[1]
        myList.insert(0, num)
    # push_back X: 정수 X를 덱의 뒤에 넣는다.
    elif text == "push_back":
        num = ip[1]
        myList.append(num)
    # pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif text == "pop_front":
        if len(myList) == 0:
            result.append(-1)
            continue
        popText = myList.pop(0)
        result.append(popText)
    # pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif text == "pop_back":
        if len(myList) == 0:
            result.append(-1)
            continue
        popText = myList.pop()
        result.append(popText)
    # size: 덱에 들어있는 정수의 개수를 출력한다.
    elif text == "size":
        result.append(len(myList))
    # empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
    elif text == "empty":
        if len(myList) == 0:
            result.append(1)
        else:
            result.append(0)
    # front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif text == "front":
        if len(myList) == 0:
            result.append(-1)
        else:
            result.append(myList[0])
    # back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif text == "back":
        if len(myList) == 0:
            result.append(-1)
        else:
            result.append(myList[len(myList) - 1])

for i in result:
    print(i)
while(True):
    n = int(input())

    if n == -1:
        break

    myList = []
    sum = 0

    for i in range(n):
        if n % (i + 1) == 0:
            myList.append(i + 1)
            sum += i + 1

    sum -= n
    myStr = ""
    if sum == n:
        myStr = str(n) + " = "
        for i, item in enumerate(myList):
            if i != len(myList) - 1:
                myStr += str(item) + " + "
        result = myStr[:-2]
        print(result)
    else:
        print(str(n) + " is NOT perfect.")



# 무지의 먹방 라이브

def solution(food_times, k):
    n = len(food_times)
    time = 0
    answer = 0
    temp = 0
    while(temp < 1000):
        for i in range(0, n):
            if(time == k):
                answer = i + 1
                break
            time += 1
            if(food_times[i] > 0):
                food_times[i] = food_times[i] - 1
                # print("food_times :", food_times)
        temp += 1
    return answer
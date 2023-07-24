import copy
def solution(arr):
    x = 0
    answer = copy.deepcopy(arr)
    while True:
        for i in range(len(answer)):
            if answer[i] >= 50 and answer[i] % 2 == 0:
                answer[i] = answer[i] // 2
            elif answer[i] < 50 and answer[i] % 2 != 0:
                answer[i] = answer[i] * 2 + 1
        
        if answer == arr:
            return x
        else:
            arr = copy.deepcopy(answer)
            x += 1
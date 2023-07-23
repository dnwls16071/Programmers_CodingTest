def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for i in range(2, total):
        side = total // i
        if (i - 2) * (side - 2) == yellow:
            answer = [i, side]
    return answer

def solution(n):
    answer = 0
    start = 1
    end = 1
    total = 0
    
    while start <= n:
        if total < n:
            total += end
            end += 1
        elif total == n:
            answer += 1
            total -= start
            start += 1
        else:
            total -= start
            start += 1
    
    return answer
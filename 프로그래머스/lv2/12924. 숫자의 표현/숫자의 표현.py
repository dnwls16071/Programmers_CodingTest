def solution(n):
    answer = 0
    start = 1
    end = 1
    total = 0
    
    # 투 포인터 사용
    # 부분합 알고리즘 활용
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
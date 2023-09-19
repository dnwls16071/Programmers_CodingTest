def solution(n, results):    
    record = [[False] * (n+1) for _ in range(n+1)]
    # A선수가 B선수를 이기는 경우 → 1
    for result in results:
        a, b = result
        record[a][b] = True
    
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if record[a][b] == True or (record[a][k] == True and record[k][b] == True):
                    record[a][b] = True
    
    answer = 0
    for a in range(1, n+1):
        cnt = 0
        for b in range(1, n+1):
            if record[a][b] == True or record[b][a] == True:
                cnt += 1
        if cnt == n-1:
            answer += 1
    return answer
# 플로이드-워셜 알고리즘 문제
# 각각의 권투선수별 스탯 차이를 2차원 배열에 기록하고 True의 개수가 n-1이 나오게 되는 경우라면 해당 권투선수의 순위를 정확히 예측할 수 있게 된다.
# 플로이드-워셜 DP 점화식을 세워 간접적으로 유추할 수 있는 권투선수별 경기 결과를 반영하고 그 다음 2중 Loop를 돌면서 True의 개수를 세어주면 된다. 
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
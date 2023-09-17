def solution(m, n, puddles):
    answer = 0
    # 좌표값 반전
    puddles = [[b, a] for a, b in puddles]
    graph = [[0] * (m+1) for _ in range(n+1)]
    graph[1][1] = 1
    
    # DP 점화식
    for b in range(1, n+1):
        for a in range(1, m+1):
            if b == 1 and a == 1:
                continue
            if [b, a] in puddles:
                graph[b][a] = 0
            else:
                graph[b][a] = (graph[b-1][a] + graph[b][a-1]) % 1000000007
    return graph[n][m]
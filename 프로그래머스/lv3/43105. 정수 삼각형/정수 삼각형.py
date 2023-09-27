def solution(triangle):
    height = len(triangle)
    dp = [[0] * height for _ in range(height)]
    dp[0][0] = triangle[0][0]
    for i in range(1, height):
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        dp[i][i] = dp[i-1][i-1] + triangle[i][i]
    
    for i in range(2, height):
        for j in range(1, i+1):
            dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
    
    for row in dp:
        Max = max(row)
    return Max
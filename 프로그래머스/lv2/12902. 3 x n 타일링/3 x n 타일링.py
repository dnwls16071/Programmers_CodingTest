# 점화식 규칙 : dp[i] = dp[i-2] * 4 - dp[i-4]
def solution(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 0
    dp[2] = 3
    dp[3] = 0
    if n < 4:
        return dp[n]
    else:
        for i in range(4, n+1):
            dp[i] = (dp[i-2] * 4 - dp[i-4]) % 1000000007
        return dp[n]
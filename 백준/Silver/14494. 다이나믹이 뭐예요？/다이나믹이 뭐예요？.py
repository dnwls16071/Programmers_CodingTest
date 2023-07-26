import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

dp = [[1 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = (dp[i-1][j] + dp[i-1][j-1] + dp[i][j-1]) % 1000000007
print(dp[n-1][m-1])
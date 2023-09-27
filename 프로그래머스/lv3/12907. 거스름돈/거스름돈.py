def solution(n, money):
    dp = [1] + [0] * n
    # 1 ~ n원까지 해당 동전을 최소 몇 개 사용하는지를 확인
    for i in money:
        for j in range(i, n+1):
            dp[j] += dp[j - i]
    return dp[n]
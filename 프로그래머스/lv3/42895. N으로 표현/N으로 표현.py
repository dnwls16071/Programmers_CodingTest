def solution(N, number):
    # 숫자 N을 1 ~ 9번 이용해서 만들 수 있는 숫자를 저장하기 위한 dp배열
    dp = [[] for _ in range(10)]
    dp[0] = [0]  # N을 0번 사용해서 만들 수 있는 숫자 → 0
    dp[1] = [N]  # N을 1번 사용해서 만들 수 있는 숫자 → 1

    # N과 number가 동일하면 바로 1을 리턴
    if N == number:
        return 1

    for i in range(2, 10):  # 2부터 9까지 반복
        nums = [int(str(N) * i)]  # 숫자를 이어붙여서 만들 수 있는 수
        for j in range(1, i // 2 + 1):  # 숫자를 j개 사용한 경우와 i-j개 사용한 경우를 고려
            for k in dp[j]:
                for m in dp[i - j]:
                    nums.append(k + m)
                    nums.append(k - m)
                    nums.append(m - k)
                    nums.append(k * m)
                    if k != 0:
                        nums.append(m // k)
                    if m != 0:
                        nums.append(k // m)
        # number는 1 이상 32000 이하
        for num in nums:
            if 1 <= num <= 32000 and num not in dp[i]:
                dp[i].append(num)

        if number in dp[i]:
            return i
    return -1

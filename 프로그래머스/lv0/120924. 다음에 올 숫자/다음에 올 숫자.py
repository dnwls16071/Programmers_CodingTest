def solution(common):
    answer = 0
    # 등차수열
    if abs(common[1] - common[0]) == abs(common[-1] - common[-2]):
        return common[-1] + (common[-1] - common[-2])
    # 등비수열
    else:
        return common[-1] * (common[-1] // common[-2])
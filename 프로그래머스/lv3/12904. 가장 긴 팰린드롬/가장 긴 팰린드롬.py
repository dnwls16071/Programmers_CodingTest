def solution(s):
    Max = 0
    for i in range(len(s)):
        for j in range(len(s)-1, -1, -1):
            if j < i:
                break
            if s[i:j+1] == s[i:j+1][::-1]:
                Max = max(Max, len(s[i:j+1]))
    return Max
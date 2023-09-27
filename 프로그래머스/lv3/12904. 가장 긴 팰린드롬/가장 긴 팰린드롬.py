# 슬라이싱을 통한 팰린드롬 참/거짓 판별
# 중복은 배제하기 위해 i의 값이 j의 값보다 커지는 경우에는 동작을 멈추도록 한다.

def solution(s):
    Max = 0
    for i in range(len(s)):
        for j in range(len(s)-1, -1, -1):
            if j < i:
                break
            if s[i:j+1] == s[i:j+1][::-1]:
                Max = max(Max, len(s[i:j+1]))
    return Max
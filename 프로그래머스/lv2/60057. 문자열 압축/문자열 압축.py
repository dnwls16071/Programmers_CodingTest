def solution(s):
    # 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이
    answer = float("INF")
    # 1개 이상부터
    for i in range(1, len(s) + 1):
        result = ""
        temp = s[:i]
        cnt = 1
        for j in range(i, len(s) + i, i):
            if temp == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    result += temp
                else:
                    result += str(cnt) + temp
                temp = s[j:j+i]
                cnt = 1
        # 가장 짧은 값을 갱신하기 위한 과정
        if answer > len(result):
            answer = len(result)
    return answer
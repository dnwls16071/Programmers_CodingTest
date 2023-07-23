def solution(my_string, overwrite_string, s):
    answer = ''
    # overwrite_string의 길이
    Len = len(overwrite_string)
    # overwrite_string 이후 나머지 부분
    answer += my_string[s+Len:]
    # 원래 문자열[:s] + 대체할 문자열 + overwrite_string 이후 나머지 부분
    result = my_string[:s] + overwrite_string + answer
    return result
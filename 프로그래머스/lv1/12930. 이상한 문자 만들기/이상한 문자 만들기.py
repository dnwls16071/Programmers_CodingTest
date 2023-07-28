def solution(s):
    answer = []
    s = list(s.split(" "))
    for i in s:
        converted_word = ""
        for idx in range(len(i)):
            if idx % 2 == 0:
                # upper()을 통한 대문자 변환
                converted_word += i[idx].upper()
            else:
                # lower()을 통한 소문자 변환
                converted_word += i[idx].lower()
        answer.append(converted_word)
    result = ' '.join(map(str, answer))
    return result
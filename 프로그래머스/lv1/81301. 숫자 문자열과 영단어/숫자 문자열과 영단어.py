def solution(s):
    result = ""
    answer = ""
    # 딕셔너리를 이용해서 key와 value를 대응시켜줌
    my_dict = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    for i in range(len(s)):
        answer += s[i]
        # 10진수의 경우
        if answer.isdigit():
            result += answer
            answer = ""
        # 10진수가 아닌 경우
        else:
            if answer in my_dict.keys():
                result += str(my_dict[answer])
                answer = ""
    return int(result)
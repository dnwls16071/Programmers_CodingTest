def solution(code):
    answer = ''
    # mode 초기값
    mode = 0
    
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] == "1":
                mode = 1
            else:
                if idx % 2 == 0:
                    answer += code[idx]
        else:
            if code[idx] == "1":
                mode = 0
            else:
                if idx % 2 != 0:
                    answer += code[idx]
    if len(answer) == 0:
        return "EMPTY"
    else:
        return answer
            
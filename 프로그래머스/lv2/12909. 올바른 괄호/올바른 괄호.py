def solution(s):
    flag = True
    
    stack = []
    for i in s:
        # 열린 괄호면?
        if i == "(":
            # 스택에 삽입
            stack.append(i)
        else:   # 닫힌 괄호면?
            # 만약 스택에 아무것도 들어있지 않다면?
            if len(stack) == 0:
                flag = False
                break
            # 스택의 마지막 원소값이 열린 괄호라면?
            if stack[-1] == "(":
                stack.pop()
    # 처리를 끝내고 난 다음 스택의 길이가 0이면?(올바른 괄호)
    if len(stack) == 0:
        return flag
    # 처리를 끝내고 난 다음 스택의 길이가 0이 아니면?(올바르지 않은 괄호)
    else:
        flag = False
        return flag
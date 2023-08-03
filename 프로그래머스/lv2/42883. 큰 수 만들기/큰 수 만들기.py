def solution(number, k):
    stack = []
    idx = k
    
    for i in range(len(number)):
        while stack and idx > 0 and stack[-1] < number[i]:
            stack.pop()
            idx -= 1
        stack.append(number[i])
    
    # 테스트케이스12번에서 오류가 발생함
    # 앞의 숫자가 뒤의 숫자보다 작은 경우가 없는 경우
    if idx != 0:
        for i in range(0, idx):
            stack.pop()
    return ''.join(map(str, stack))

# 테스트케이스 "1924", k = 2
#1 stack = [1]
#2 stack = [9]
#3 stack = [9, 2]
#4 stack = [9, 4] → 따라서, "94"

# 테스트케이스 "54321", k = 1
# result : "5432"
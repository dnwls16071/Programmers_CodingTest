from itertools import permutations
from collections import deque

# 연산 함수
def operation(num1, num2, op):
    if op == '+':
        return int(num1) + int(num2)
    elif op == '-':
        return int(num1) - int(num2)
    elif op == '*':
        return int(num1) * int(num2)
    

def calculate(exp, op):
    array = deque()
    tmp = ""
    for i in exp:
        if i.isdigit() == True:
            tmp += i
        else:
            array.append(tmp)
            array.append(i)
            tmp = ""
    array.append(tmp)
    
    for o in op:
        stack = deque()
        while len(array) != 0:
            tmp = array.popleft()
            if tmp == o:
                stack.append(operation(stack.pop(), array.popleft(), o))
            else:
                stack.append(tmp)
        array = stack
    return abs(int(array[0]))


def solution(expression):
    op = ['+', '-', '*']
    # 연산자의 우선순위 조합에 따른 경우의 수
    op = list(permutations(op, 3))
    result = []
    for i in op:
        result.append(calculate(expression, i))
    return max(result)
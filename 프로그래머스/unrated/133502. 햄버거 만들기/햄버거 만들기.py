# [2, 1, 1, 2, 3, 1, 2, 3, 1]
# 첫 번째 햄버거 : [1, 2, 3, 1] 완성 후 리스트의 상태 : [2, 1, 2, 3, 1]
# 두 번째 햄버거 : [1, 2, 3, 1] 완성 후 리스트의 상태 : [2]
def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if str(''.join(map(str, stack[-4:]))) == "1231":
            answer += 1
            for _ in range(4):
                stack.pop()
    return answer
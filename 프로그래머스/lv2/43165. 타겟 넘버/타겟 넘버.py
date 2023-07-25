from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((0, 0))    # 배열 순서, 합계
    while queue:
        sequence, Sum = queue.popleft()
    
        if sequence >= len(numbers):
            break

        queue.append((sequence+1, Sum + numbers[sequence]))
        queue.append((sequence+1, Sum - numbers[sequence]))
    
    result = list(queue)
    for i in result:
        if i[1] == target:
            answer += 1
    return answer
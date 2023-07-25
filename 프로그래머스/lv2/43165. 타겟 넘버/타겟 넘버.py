from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((0, 0))    # 배열 순서, 합계
    while queue:
        sequence, Sum = queue.popleft()
    
        # ex. len(numbers) = 5, sequence = 6 ( X )
        if sequence > len(numbers):
            break
        
        # ex. len(numbers) = 5, sequence = 5
        elif sequence == len(numbers) and Sum == target:
            answer += 1

        if sequence == len(numbers):
            continue
        else:
            queue.append((sequence+1, Sum + numbers[sequence]))
            queue.append((sequence+1, Sum - numbers[sequence]))
    return answer
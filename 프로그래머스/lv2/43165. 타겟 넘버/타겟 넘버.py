#1
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
    
    ### queue에 저장된 데이터를 확인할 방법이 없어 결국 list로 변환하여 작성하는 방법을 택함
    ### while문에 넣어 만들어진 수의 합이 타겟 넘버와 일치하는지를 판단하는 분기문을 넣어 해결하는 방법 다시 생각할 것
    ### 
    result = list(queue)
    for i in result:
        if i[1] == target:
            answer += 1
    ###
    return answer

#2
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
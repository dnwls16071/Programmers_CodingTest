# 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.

# 스택과 큐를 이용해서 해결하고자 코드를 작성했으나 해결하지 못하고 결국 [질문하기]에서 확인한 해결 방법을 적용한 문제★★★
from collections import deque

def solution(priorities, location):
    sequence = 0
    queue = deque(enumerate(priorities))
    temp = priorities[location]
    temp_idx = location
    
    while queue:
        idx, priority = queue.popleft()
        if any(priority < val for idx, val in queue):
            queue.append((idx, priority))
        else:
            sequence += 1
            if idx == temp_idx and priority == temp:
                return sequence
        
# location : 몇 번째로 실행이 되는지 알고 싶은 것(0번째부터 계산)

# 테스트케이스1 이해 → 2번째(즉, C가 몇 번째로 실행이 되느냐?)
# location = [0, 1, 2, 3], priorities = [A, B, C, D]
# 프로세스 4개 : [A, B, C, D], 우선순위 : [2, 1, 3, 2]
# 각각의 프로세스 [A, B, C, D]가 몇 번째로 실행이 되는 것인가?

# C(1), D(2), A(3), B(4)

# 테스트케이스2 이해 → 0번째(즉, A가 몇 번째로 실행이 되느냐?)
# 프로세스 6개 : [A, B, C, D, E, F], 우선순위 : [1, 1, 9, 1, 1, 1]
# 각각의 프로세스 [A, B, C, D, E, F]가 몇 번째로 실행이 되는 것인가?

# C(1), D(2), E(3), F(4), A(5), B(6)

# python any함수 → any 함수는 인자로 받은 요소 중 하나라도 참이 있으면 True를 반환하고, 모든 요소가 거짓이면 False를 반환한다.
def any(iterable):
    for element in iterable:
    	if element:
        	return True
    return False

# python all함수 → all 함수는 인자로 받은 모든 요소가 참이어야 True를 반환하고 하나라도 거짓이면 False를 반환한다.
def all(iterable):
	for element in iterable:
    	if not element:
        	return False
    return True

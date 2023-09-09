# x에 n을 더합니다    → y에서 n을 뺀다.
# x에 2를 곱합니다.   → y에서 2를 나눈다.
# x에 3을 곱합니다.   → y에서 3을 나눈다.
from collections import deque

def solution(x, y, n):
    cnt = 0
    queue = deque()
    queue.append([x, cnt])
    visited = set()
    while queue:
        v, cnt = queue.popleft()
        # 도달해야하는 값 y보다 큰 경우거나 이미 방문한 이력이 있다면?
        if v > y or v in visited:
            continue
            
        # 만약 x가 y와 일치하는 경우가 존재한다면?
        if v == y:
            return cnt
        
        visited.add(v)
        # 세 가지 연산 Loop
        for i in [v*3, v*2, v+n]:
            if i not in visited and i <= y:
                queue.append([i, cnt + 1])
    return -1
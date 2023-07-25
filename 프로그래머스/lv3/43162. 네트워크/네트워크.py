# BFS 코드
from collections import deque

def solution(n, computers):
    def BFS(v):
        queue = deque()
        queue.append(v)
        while queue:
            start = queue.popleft()
            
            for i in range(n):
                if not visited[i] and computers[start][i] == 1:
                    visited[i] = True
                    queue.append(i)
        
    visited = [False] * (n+1)
    network = 0
    
    for i in range(n):
        if not visited[i]:
            BFS(i)
            network += 1
    return network
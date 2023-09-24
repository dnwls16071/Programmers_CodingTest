from collections import deque

def solution(n, edge):
    visited = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for e in edge:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)
    res = BFS(1, graph, visited)
    Max = max(visited)
    cnt = 0
    # 출발점인 1번 노드는 제외한 나머지 노드를 대상으로 1번 노드로부터 가장 멀리 떨어진 노드의 개수를 확인
    for i in range(2, len(visited)):
        if res[i] == Max:
            cnt += 1
    return cnt

def BFS(start, graph, visited):
    queue = deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)
    return visited
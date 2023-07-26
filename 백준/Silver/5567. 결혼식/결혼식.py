from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
relationship = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().strip().split())
    relationship[a].append(b)
    relationship[b].append(a)


def BFS(graph, start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        start = queue.popleft()
        for i in graph[start]:
            if not visited[i]:
                visited[i] = visited[start] + 1
                queue.append(i)
    return visited


visited = [0] * (n + 1)
BFS(relationship, 1)
friend = 0
visited = [False] * (n + 1)
li = BFS(relationship, 1)
for i in li:
    if i < 4 and i > 0:
        friend += 1
print(friend - 1)
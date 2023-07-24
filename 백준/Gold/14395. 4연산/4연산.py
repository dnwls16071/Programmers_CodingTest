from collections import deque
import sys
input = sys.stdin.readline

def BFS(start, result):
    queue = deque()
    if s == t:
        return 0
    queue.append((start, ""))
    visited.add(start)
    while queue:
        v, op = queue.popleft()
        if v == t:
            return op

        if v * v <= 1e9 and v * v not in visited:
            visited.add(v * v)
            queue.append((v * v, op + "*"))

        if v + v <= 1e9 and v + v not in visited:
            visited.add(v + v)
            queue.append((v + v, op + "+"))

        if 0 not in visited:
            visited.add(0)
            queue.append((v - v, op + "-"))

        if s != 0 and s >= 1 and 1 not in visited:
            visited.add(1)
            queue.append((v // v, op + "/"))
    return -1


s, t = map(int, input().strip().split())
visited = set()
print(BFS(s, ""))
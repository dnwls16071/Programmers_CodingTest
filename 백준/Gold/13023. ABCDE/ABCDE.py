from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().strip().split())
camp = [[] for _ in range(N)]
visited = [False] * N
flag = False
for _ in range(M):
    a, b = map(int, input().strip().split())
    camp[a].append(b)
    camp[b].append(a)

def DFS(v, depth):
    global flag
    visited[v] = True
    if depth == 5:
        flag = True
        return
    for i in camp[v]:
        if not visited[i]:
            visited[i] = True
            DFS(i, depth + 1)
            visited[i] = False

for i in range(N):
    visited[i] = True
    DFS(i, 1)
    visited[i] = False
    if flag:
        break

if flag:
    print(1)
else:
    print(0)
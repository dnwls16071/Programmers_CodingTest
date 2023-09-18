from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
chess = [[0] * N for _ in range(N)]
r1, c1, r2, c2 = map(int, input().strip().split())

def BFS(a, b):
    queue = deque()
    queue.append([a, b])
    chess[a][b] = 0
    while queue:
        r, c = queue.popleft()

        dr = [0, 2, 2, 0, -2, -2]
        dc = [-2, -1, 1, 2, 1, -1]
        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if 0 <= nr < N and 0 <= nc < N and not chess[nr][nc]:
                chess[nr][nc] = chess[r][c] + 1
                queue.append([nr, nc])
    return chess

result = BFS(r1, c1)
if result[r2][c2] == 0:
    print(-1)
else:
    print(result[r2][c2])
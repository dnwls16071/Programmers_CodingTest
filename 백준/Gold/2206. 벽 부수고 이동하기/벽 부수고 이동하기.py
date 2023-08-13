from collections import deque
import sys
input = sys.stdin.readline

def BFS(y, x, z):
    queue = deque()
    queue.append((y, x, z))
    while queue:
        a, b, c = queue.popleft()
        if a == N-1 and b == M-1:
            return visited[a][b][c]
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = b + dx[i]
            ny = a + dy[i]
            # 영역 밖의 경우
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            # visited[y][x][0] : 벽을 부수고 이동하는 경우를 나타내는 방문 배열
            # visited[y][x][1] : 벽을 부수지 않고 이동하는 경우를 나타내는 방문 배열
            if 0 <= nx < M and 0 <= ny < N:
                # 해당 좌표가 벽이고 벽 파괴 기회를 사용하지 않은 경우
                if graph[ny][nx] == 1 and c == 0:
                    visited[ny][nx][1] = visited[a][b][c] + 1
                    queue.append((ny, nx, 1))
                # 해당 좌표가 벽이 아니고 방문하지 않은 곳이라면?
                elif graph[ny][nx] == 0 and not visited[ny][nx][c]:
                    visited[ny][nx][c] = visited[a][b][c] + 1
                    queue.append((ny, nx, c))
    return -1

N, M = map(int, input().strip().split())
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))
print(BFS(0, 0, 0))
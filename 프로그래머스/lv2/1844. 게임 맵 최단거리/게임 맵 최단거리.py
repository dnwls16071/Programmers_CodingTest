from collections import deque

def solution(maps):
    height = len(maps)          # 세로
    width = len(maps[0])        # 가로
    visited = [[False] * width for _ in range(height)]
    queue = deque()
    queue.append((0, 0))
    while queue:
        y, x = queue.popleft()
        
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                continue
            if 0 <= nx < width and 0 <= ny < height and maps[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    maps[ny][nx] = maps[y][x] + 1

    if visited[height-1][width-1]:
        return maps[height-1][width-1]
    else:
        return -1
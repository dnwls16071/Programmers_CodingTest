import sys
input = sys.stdin.readline

N = int(input())
digit_number = int(input())
table = [[0] * N for _ in range(N)]

current_number = N * N
x, y = 0, 0
direction = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while current_number >= 1:
    table[y][x] = current_number

    if current_number == digit_number:
        target_x, target_y = x, y

    next_x, next_y = x + dx[direction], y + dy[direction]

    if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N or table[next_y][next_x] != 0:
        direction = (direction + 1) % 4

    x, y = x + dx[direction], y + dy[direction]
    current_number -= 1

for row in table:
    print(" ".join(map(str, row)))

for i in range(N):
    for j in range(N):
        if table[i][j] == digit_number:
            print(i+1, j+1)
            break
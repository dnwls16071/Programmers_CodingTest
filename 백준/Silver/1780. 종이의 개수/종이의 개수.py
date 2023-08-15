import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
papers = []
for _ in range(N):
    papers.append(list(map(int, input().strip().split())))

def recursive(x, y, N):
    global result
    paper = papers[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if papers[i][j] != paper:
                for k in range(3):
                    for t in range(3):
                        recursive(x + k * N//3, y + t * N//3, N//3)
                return
    if paper == 0:
        result[0] += 1
    elif paper == 1:
        result[1] += 1
    else:
        result[-1] += 1

result = [0, 0, 0]
recursive(0, 0, N)
print(result[-1], result[0], result[1])
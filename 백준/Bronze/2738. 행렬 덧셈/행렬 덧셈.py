import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

A = []
B = []

for i in range(N):
    A.append(list(map(int ,input().strip().split())))

for i in range(N):
    B.append(list(map(int, input().strip().split())))

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end = " ")
    print()
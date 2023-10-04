from collections import deque
import sys
input = sys.stdin.readline

def solve(N, K, A):
    res = 0
    belt = deque([False] * N)

    while True:
        res += 1

        A.rotate(1)
        belt.rotate(1)

        belt[N-1] = False
        for i in range(N-2, -1, -1):
            if A[i+1] > 0 and belt[i] and not belt[i+1]:
                belt[i], belt[i+1] = False, True
                A[i+1] -= 1
        belt[N-1] = False

        if A[0] > 0:
            belt[0] = True
            A[0] -= 1

        if A.count(0) >= K:
            break
    return res

N, K = map(int, input().strip().split())
A = deque(map(int, input().strip().split()))
print(solve(N, K, A))
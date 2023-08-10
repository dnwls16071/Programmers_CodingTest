from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N = int(input())
coding = list(map(int, input().strip().split()))
coding.sort()
cnt = 0

for a in range(N-1):
    for b in range(a+1, N):
        temp = (coding[a] + coding[b]) * -1
        cnt += bisect_right(coding, temp, a+1, b) - bisect_left(coding, temp, a+1, b)
print(cnt)
import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().strip().split()))
min_value = float('INF')

start = 0
end = N-1
while start < end:
    if abs(liquid[start] + liquid[end]) < abs(min_value):
        min_value = liquid[start] + liquid[end]

    if liquid[start] + liquid[end] > 0:
        end -= 1
    elif liquid[start] + liquid[end] < 0:
        start += 1
    else:
        break
print(min_value)
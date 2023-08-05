from itertools import permutations

N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

for i in permutations(li, M):
    print(*i)
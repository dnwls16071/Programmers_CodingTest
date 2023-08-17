import sys
input = sys.stdin.readline

n = int(input())
A = []
B = []
C = []
D = []
for i in range(n):
    a, b, c, d = map(int, input().strip().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab_dict = {}
for a in A:
    for b in B:
        if a + b not in ab_dict:
            ab_dict[a + b] = 1
        else:
            ab_dict[a + b] += 1

result = 0
for c in C:
    for d in D:
        if -(c + d) in ab_dict:
            result += ab_dict[-(c + d)]
print(result)
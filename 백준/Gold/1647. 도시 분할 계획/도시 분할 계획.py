import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().strip().split())
parent = [0] * (N+1)
edges = []
selected = []

for i in range(1, N+1):
    parent[i] = i

for _ in range(M):
    A, B, C = map(int, input().strip().split())
    edges.append([C, A, B])
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        selected.append(cost)

selected.sort()
selected.pop()
print(sum(selected))
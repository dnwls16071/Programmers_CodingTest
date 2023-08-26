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

N = int(input())
parent = [0] * (N+1)
edges = []
result = 0

for i in range(1, N+1):
    parent[i] = i

x_planet = []
y_planet = []
z_planet = []
for i in range(1, N+1):
    x, y, z = map(int, input().strip().split())
    x_planet.append([x, i])
    y_planet.append([y, i])
    z_planet.append([z, i])

x_planet.sort()
y_planet.sort()
z_planet.sort()
# 2중 루프로 인한 메모리초과
# for i in range(N-1):
#     for j in range(i+1, N):
#         edges.append([min(abs(planet[i][0] - planet[j][0]), abs(planet[i][1] - planet[j][1]), abs(planet[i][2] - planet[j][2])), i, j])
for i in range(N-1):
    edges.append([abs(x_planet[i+1][0] - x_planet[i][0]), x_planet[i][1], x_planet[i+1][1]])
    edges.append([abs(y_planet[i+1][0] - y_planet[i][0]), y_planet[i][1], y_planet[i+1][1]])
    edges.append([abs(z_planet[i+1][0] - z_planet[i][0]), z_planet[i][1], z_planet[i+1][1]])
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
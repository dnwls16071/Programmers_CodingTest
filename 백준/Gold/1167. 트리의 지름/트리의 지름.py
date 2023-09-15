from collections import deque
import sys
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    lst = list(map(int, input().strip().split()))
    prev_node = lst[0]
    for i in range(1, len(lst), 2):
        if lst[i] == -1:
            break
        else:
            next_node, cost = lst[i], lst[i+1]
            graph[prev_node].append([next_node, cost])
            graph[next_node].append([prev_node, cost])

def BFS(start, prefix_sum, result):
    queue = deque()
    queue.append([start, prefix_sum])
    while queue:
        s, p = queue.popleft()
        for i in graph[s]:
            node, cost = i
            if result[node] == -1:
                queue.append([node, cost])
                result[node] = result[s] + cost
    return result

result = [-1] * (V+1)
result[1] = 0
BFS(1, 0, result)
num = result.index(max(result))

result = [-1] * (V+1)
result[num] = 0
BFS(num, 0, result)
print(max(result))
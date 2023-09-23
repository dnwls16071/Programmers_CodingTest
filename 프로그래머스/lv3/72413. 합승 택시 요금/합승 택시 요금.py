# 단방향으로 이동(이동방향에 따라 달라지지 않는다.)
# 다익스트라 알고리즘을 통한 최단 거리 갱신
import heapq

def solution(n, s, a, b, fares):
    Min = int(1e9)
    graph = [[] for _ in range(n+1)]
    distance = [[]]
    for c, d, f in fares:
        graph[c].append([d, f])
        graph[d].append([c, f])
    
    for i in range(1, n+1):
        distance.append(dijkstra(i, n, graph))
    
    for i in range(1, n+1):
        Min = min(Min, distance[s][i] + distance[i][a] + distance[i][b])
    return Min

def dijkstra(start, n, graph):
    INF = int(1e9)
    res = [INF] * (n + 1)
    res[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    while q:
        dist, now = heapq.heappop(q)
        if res[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if res[i[0]] > cost:
                res[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
    return res
# 양방향으로 통핼할 수 있는 도로로 연결됨 → 양방향 그래프
# N개의 마을 중에서 K시간 이하로 배달기 가능한 마을에만 배달이 가능
# 다익스트라 알고리즘으로 각 노드에 대한 최단 경로를 갱신한 후 K시간보다 큰 값이 나오면 해당 마을을 배달 안하면 됨
# 1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 리턴하라. → 출발 노드는 1번 노드다.
import heapq

def solution(N, road, K):
    INF = int(1e9)
    graph = [[] for _ in range(N+1)]    # 그래프의 인접한 노드를 저장
    distance = [INF] * (N+1)              # 최단 경로 테이블
    for r in road:
        a, b, c = r
        graph[a].append([b, c])
        graph[b].append([a, c])
    result = dijkstra(1, distance, graph)
    tot = 0
    for village in result:
        if village <= K:
            tot += 1
    return tot

# 다익스트라 알고리즘 소스 코드
def dijkstra(start, distance, graph):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
    return distance
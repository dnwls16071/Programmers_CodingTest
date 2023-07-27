import heapq

def solution(d, budget):
    # 오름차순으로 정렬
    heap = d
    heapq.heapify(heap)
    
    answer = 0
    while heap:
        a = heapq.heappop(heap)
        budget -= a
        if budget < 0:
            break
        answer += 1
    return answer
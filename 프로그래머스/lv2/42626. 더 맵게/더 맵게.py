# 힙 자료구조는 자동 정렬을 보장함
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if scoville[0] >= K:
            break
        
        try:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + b * 2)
            answer += 1
        except IndexError:
            return -1
    return answer

# 테스트케이스[1, 3, 8, 14] 런타임 에러 발생 → 발생 이유 : 힙에 들어있는 원소의 개수가 만약 반환해야하는 값의 개수인 2개보다 작은 경우

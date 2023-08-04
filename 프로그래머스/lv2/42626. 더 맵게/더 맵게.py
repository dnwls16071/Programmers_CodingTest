# 힙 자료구조는 자동 정렬을 보장함
# try ~ except 예외처리를 사용

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        # 첫 원소의 스코빌 지수가 K이상이면 그 이후의 원소는 다 K를 넘는 것이므로
        if scoville[0] >= K:
            break
        
        try:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + b * 2)
            answer += 1
        # 아래 주석의 경우 런타임에러(정확하게 발생하는 에러는 인덱스에러)
        except IndexError:
            return -1
    return answer

# 테스트케이스[1, 3, 8, 14] 런타임 에러 발생 → 발생 이유 : 힙에 들어있는 원소의 개수가 만약 반환해야하는 값의 개수인 2개보다 작은 경우

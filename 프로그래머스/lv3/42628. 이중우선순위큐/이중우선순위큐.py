# # 하나의 힙으로 문제를 해결하는 방법
# import heapq

# def solution(operations):
#     queue = []
#     heapq.heapify(queue)
    
#     for op in operations:
#         op = list(op.split(" "))
#         if op[0] == "I":
#             heapq.heappush(queue, int(op[1]))
#         # 최댓값을 삭제하는 명령
#         elif op[0] == "D" and int(op[1]) == 1:
#             if len(queue) != 0:
#                 Max_element = max(queue)
#                 queue.remove(Max_element)
#         # 최솟값을 삭제하는 명령
#         elif op[0] == "D" and int(op[1]) == -1:
#             if len(queue) != 0:
#                 heapq.heappop(queue)
    
#     if queue:
#         Max_value = max(queue)
#         Min_value = min(queue)
#         return [Max_value, Min_value]
#     else:
#         return [0, 0]

# 두 개의 힙으로 우선순위 큐를 구현해 문제를 해결하는 방법
import heapq

def solution(operations):
    answer = []
    minH, maxH = [], []
    for op in operations:
        op = list(op.split(" "))
        op[1] = int(op[1])
        if op[0] == "I":
            heapq.heappush(minH, op[1])     # 최소힙은 힙의 디폴트 기능
            heapq.heappush(maxH, -op[1])    # 최대힙은 음수로 구현 가능
        else:
            if not maxH or not minH:
                continue
            if op[1] == 1:
                minH.remove(-heapq.heappop(maxH))
            elif op[1] == -1:
                maxH.remove(-heapq.heappop(minH))
    if maxH or minH:
        return [-heapq.heappop(maxH), heapq.heappop(minH)]
    else:
        return [0, 0]
    
    
    # 테스트케이스1 작동 과정
    # min_H : [123]
    # max_H : [123]
    # actual_array : [] → [0, 0]
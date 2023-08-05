import heapq

def solution(operations):
    queue = []
    heapq.heapify(queue)
    
    for op in operations:
        op = list(op.split(" "))
        if op[0] == "I":
            heapq.heappush(queue, int(op[1]))
        # 최댓값을 삭제하는 명령
        elif op[0] == "D" and int(op[1]) == 1:
            if len(queue) != 0:
                Max_element = max(queue)
                queue.remove(Max_element)
        # 최솟값을 삭제하는 명령
        elif op[0] == "D" and int(op[1]) == -1:
            if len(queue) != 0:
                heapq.heappop(queue)
    
    if queue:
        Max_value = max(queue)
        Min_value = min(queue)
        return [Max_value, Min_value]
    else:
        return [0, 0]
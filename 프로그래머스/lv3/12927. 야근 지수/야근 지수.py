# 야근 피로도 : 야근을 시작한 시점에서 남은 일의 작업량의 제곱하여 더한 값
# 야근 피로도를 최소화하려면 결국 작업량이 가장 높은 데이터에 대해서 1시간씩 작업을 수행하고 정렬을 수행하여 매번 과정을 반복해야함
# 효율성 측면에서 실패 결과를 받은 코드 → 로직 자체에는 문제가 없지만 더 효율적인 방법이 존재함(힙)
def solution(n, works):
    result = 0
    while n != 0:
        works.sort(reverse=True)
        works[0] -= 1
        n -= 1

    for i in works:
        if i <= 0:
            continue
        else:
            result += i**2
    return result

import heapq

def solution(n, works):
    result = 0
    works = [-i for i in works]
    heapq.heapify(works)
    while n != 0:
        if works[0] == 0:
            break
        temp = heapq.heappop(works)
        n -= 1
        temp += 1
        heapq.heappush(works, temp)
    
    works = [-i for i in works]
    for work in works:
        result += work ** 2
    return result
# 정렬을 이용한 풀이
def solution(k, m, score):
    # 배열 내림차순으로 정렬
    score.sort(reverse=True)
    
    # 얻을 수 있는 최대 이익
    profit = 0
    result = []
    for i in range(0, len(score), m):
        if i + m <= len(score):
            profit += min(score[i:i+m]) * m
    return profit

# 최대 힙과 깊은 복사를 이용한 풀이
import heapq
import copy

def solution(k, m, score):
    score = [-i for i in score]
    heapq.heapify(score)
    temp = copy.deepcopy(score)
    
    profit = 0
    result = []
    for i in range(len(temp)):
        if len(result) == m:
            profit += min(result) * m
            result = []
        result.append(-heapq.heappop(score))
    # 위에서 조건은 만족하지만 인덱싱이 다 돌아 처리하지 못한 result 배열의 길이가 m인 경우 마지막으로 처리
    if len(result) == m:
        profit += min(result) * m
    return profit
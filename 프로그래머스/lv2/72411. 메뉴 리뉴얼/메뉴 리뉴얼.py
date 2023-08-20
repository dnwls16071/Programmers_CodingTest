# 테스트케이스 [4, 5, 7, 9, 19, 20] 오류
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        result = Counter()
        lst = [len(order) for order in orders]
        maximum_comb = max(lst)
        
        for order in orders:
            if c > maximum_comb:
                continue
            menu_comb = list(combinations(sorted(order), c))
            result += Counter(menu_comb)
        
        max_value = max(result.values(), default=0)  # 빈 시퀀스에서도 기본값 0으로 초기화
        
        for key, value in result.items():
            if value == max_value and value >= 2:
                answer.append(''.join(map(str, key)))
    
    answer.sort()
    return answer
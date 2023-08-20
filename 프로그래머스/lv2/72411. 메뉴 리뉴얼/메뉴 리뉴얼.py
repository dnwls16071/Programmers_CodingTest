from itertools import combinations  # itertools 모듈 사용
from collections import Counter     # Counter 클래스 사용

def solution(orders, course):
    answer = []         # 새로 추가하게 될 코스요리의 메뉴 구성 문자열을 저장하는 리스트
    for c in course:
        result = Counter()      
        lst = [len(order) for order in orders]  # 코스요리 메뉴 구성의 길이
        maximum_comb = max(lst)                 # 최댓값(만약 코스요리의 메뉴 중에서 가장 큰 값이 c보다 작을 경우 추가할 수 없으므로)
        
        for order in orders:
            if c > maximum_comb:
                continue
            menu_comb = list(combinations(sorted(order), c))    # 배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬
            result += Counter(menu_comb)                        # 빈도 수를 계산해서 result 변수에 누적
        
        max_value = max(result.values(), default=0)  # 빈 시퀀스에서도 기본값 0으로 초기화
        for key, value in result.items():
            if value == max_value and value >= 2:   # 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 후보에 포함하므로
                answer.append(''.join(map(str, key)))
    answer.sort()
    return answer
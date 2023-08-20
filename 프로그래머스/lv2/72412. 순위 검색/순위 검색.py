# [효율성 테스트] : 100
# [정확성 테스트] : 테스트케이스 [2, 3, 4, 7, 13, 16] 에러
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left, bisect_right

def solution(info, query):
    result = []
    # 런타임에러 방지
    comb_dict = defaultdict(int)
    
    for i in range(len(info)):
        information = info[i].split(" ")
        comb_key = information[:-1]
        comb_value = int(information[-1])
        for i in range(5):
            for c in combinations(comb_key, i):
                comb_temp = ''.join(map(str, c))
                if comb_temp not in comb_dict:
                    comb_dict[comb_temp] = [comb_value]
                else:
                    comb_dict[comb_temp].append(comb_value)
    
    # 조합에 해당하는 점수를 오름차순으로 정렬 → 이진 탐색을 이용하기 위해서
    for item in comb_dict:
        comb_dict[item].sort()
    
    for q in query:
        q = q.replace("and", "")
        q = list(q.split())
        # 하이픈(-)은 해당 조건을 고려하지 않는 것 → 특정 값을 나타내는 것이 아니므로 전부 제거
        while '-' in q:     
            q.remove('-')
        q_info = q[:-1]
        q_score = int(q[-1])
        query_key = ''.join(map(str, q_info))
        if query_key in comb_dict:
            # [조건]을 만족하면서 최소 x점 이상인 사람들만 합격이 가능함
            bisect_left_value_index = bisect_left(comb_dict[query_key], q_score)
            result.append(len(comb_dict[query_key]) - bisect_left_value_index)
        else:
            # [조건]을 만족하지 않으므로 결국 0을 추가
            result.append(0)
    return result
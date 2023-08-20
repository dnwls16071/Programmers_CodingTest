# [효율성 테스트] : 100
# [정확성 테스트] : 테스트케이스 [2, 3, 4, 7, 13, 16] 에러
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left, bisect_right

def solution(info, query):
    result = []
    # Keyerror 방지
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
    
    for item in comb_dict:
        comb_dict[item].sort()
        
    for key in comb_dict:
        comb_dict[key] = sorted(comb_dict[key])  # Sort values in the dictionary
    
    for q in query:
        q = q.replace("and", "")
        q = list(q.split())
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
            result.append(0)
    return result
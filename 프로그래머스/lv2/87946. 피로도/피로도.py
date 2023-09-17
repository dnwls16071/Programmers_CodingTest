from itertools import permutations

def solution(k, dungeons):
    lst = permutations(dungeons)
    res = []
    # 던전 탐험 순열
    for i in lst:
        res.append(i)
    
    tot = 0
    for i in res:
        K = k
        temp = 0
        for j in i:
            # a : 최소 필요 피로도, b : 소모 피로도
            a, b = j[0], j[1]
            if K >= a and K - b >= 0:
                K -= b      # 피로도 갱신
                temp += 1    # 탐험가능한 던전의 숫자
            else:
                break
        tot = max(tot, temp)
    return tot
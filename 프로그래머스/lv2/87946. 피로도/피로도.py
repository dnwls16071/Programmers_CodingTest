from itertools import permutations

def solution(k, dungeons):
    lst = permutations(dungeons)
    res = []
    # 던전 탐험 순열
    for i in lst:
        res.append(i)
    
    tot = 0
    for i in res:
        K = k           # 유저의 현재 피로도
        temp = 0        # 탐험가능한 던전의 갯수
        for j in i:
            # a : 최소 필요 피로도, b : 소모 피로도
            a, b = j[0], j[1]
            if K >= a and K - b >= 0:   # 유저의 현재 피로도가 최소 필요 피로도 이상 & 유저의 현재 피로도에서 소모 피로도를 뺀 값이 0이상
                K -= b      # 피로도 갱신
                temp += 1   
            else:
                break
        tot = max(tot, temp)    # 최댓값 갱신
    return tot
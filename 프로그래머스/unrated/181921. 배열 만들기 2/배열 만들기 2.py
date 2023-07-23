# 중복순열을 사용하여 문제를 해결
# 선형탐색을 진행하기에는 매우 많은 시간이 걸릴 것으로 판단함
from itertools import product

def solution(l, r):
    answer = []
    
    for i in range(len(str(l)), len(str(r))+1):
        for j in product([0, 5], repeat = i):
            j = int(''.join(map(str, j)))
            if l <= j and j <= r and j not in answer:
                answer.append(j)
    if len(answer) == 0:
        return [-1]
    else:
        return answer
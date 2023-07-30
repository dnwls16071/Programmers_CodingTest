#1. itertools 모듈과 조합론을 이용한 풀이
from itertools import permutations

def solution(numbers):
    answer = []
    for i in permutations(numbers, 2):
        temp = sum(i)
        if temp not in answer:
            answer.append(temp)
    answer.sort()
    return answer

#2. 백트래킹을 이용한 풀이
def solution(numbers):
    def backtrack(start, lst):
        if len(lst) == 2:
            result.add(sum(lst))
            return
        for i in range(start, len(numbers)):
            backtrack(i + 1, lst + [numbers[i]])

    result = set()
    backtrack(0, [])
    return sorted(list(result))
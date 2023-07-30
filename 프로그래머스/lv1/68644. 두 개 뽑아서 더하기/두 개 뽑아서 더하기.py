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
    # 백트래킹 함수 구현
    def backtrack(start, lst):
        # 두 개의 숫자를 뽑으면 뽑은 숫자의 합을 추가
        if len(lst) == 2:
            result.add(sum(lst))
            return
        # 서로 다른 인덱스에 있는 두 개의 수를 뽑는 것이므로 중복이 안됨
        for i in range(start, len(numbers)):
            backtrack(i + 1, lst + [numbers[i]])

    result = set()
    backtrack(0, [])
    return sorted(list(result))
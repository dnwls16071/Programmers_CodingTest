from itertools import permutations

def solution(numbers):
    answer = []
    for i in permutations(numbers, 2):
        temp = sum(i)
        if temp not in answer:
            answer.append(temp)
    answer.sort()
    return answer
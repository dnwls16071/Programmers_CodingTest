# 한 문자의 최대 빈도는 4, 전체 모음 문자의 개수는 5개, 따라서 중복순열로 해결해도 괜찮지않을까?
# 재귀함수를 이용한 풀이도 가능할 것 같은데 조금 더 고민해볼것
from itertools import product

def solution(word):
    answer = []
    arr = ['A','E','I','O','U']
    for i in range(1, 6):
        for j in product(arr, repeat=i):
            answer.append(''.join(map(str, j)))
    answer.sort()
    result = 0
    for ans in answer:
        if ans == word:
            return result + 1
        result += 1
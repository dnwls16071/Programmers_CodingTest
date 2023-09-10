# 중복순열로 해결하는 방법
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
        
# 재귀 알고리즘
import sys
sys.setrecursionlimit(10**6)

def recursive(answer, step, p):
    arr = ['A','E','I','O','U']
    if step == 6:
        return
    if p != "":
        answer.append(p)
    for i in range(len(arr)):
        recursive(answer, step+1, ''.join([p, arr[i]]))
    
def solution(word):
    rank = 0
    answer = []
    recursive(answer, rank, "")
    for i in range(len(answer)):
        if answer[i] == word:
            rank = i + 1
            break
    return rank
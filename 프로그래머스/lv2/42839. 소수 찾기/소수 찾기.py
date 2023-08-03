# 0 ~ 9,999,999 즉, 10,000,000 길이만큼의 배열을 만들어 에라토스테네스의 체로 소수를 판정하면 메모리 초과가 발생함
# itertools 모듈의 permutations와 DFS 탐색을 활용한 방법
# 소수 판정 알고리즘
from itertools import permutations

def isprime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    arr = []
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            if isprime(int(''.join(map(str, j)))) and int(''.join(map(str, j))) not in arr:
                arr.append(int(''.join(map(str, j))))
    return len(arr)
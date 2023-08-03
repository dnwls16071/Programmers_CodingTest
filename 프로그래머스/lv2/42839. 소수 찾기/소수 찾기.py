# 0 ~ 9,999,999 즉, 10,000,000 길이만큼의 배열을 만들어 에라토스테네스의 체로 소수를 판정하면 메모리 초과가 발생함
#1. itertools 모듈의 permutations을 이용한 방법
from itertools import permutations

# 소수 판정 알고리즘
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

#2. BFS 완전 탐색을 이용한 방법
from collections import deque, Counter

def solution(numbers):
    # 소수 판정 알고리즘
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    # BFS 완전 탐색
    def BFS(start, length, remaining):
        prime_count = set()
        queue = deque()
        queue.append([start, length, remaining])
        
        while queue:
            curr_num, length, remaining = queue.popleft()
            
            # 만약 길이가 numbers의 길이 이하이면서 해당 숫자가 소수라면?
            if 1 <= length <= len(numbers) and is_prime(curr_num):
                prime_count.add(int(curr_num))
            
            for i in range(len(remaining)):
                [num, count] = remaining[i]
                if (1 <= length <= len(numbers) or (length == 0 and num != 0)) and count > 0:
                    # 1 → 1 * 10 + 7 테크닉 활용
                    new_num = curr_num * 10 + num
                    new_remaining = remaining[:]
                    new_remaining[i] = [num, count - 1]
                    queue.append((new_num, length + 1, new_remaining))
        
        return prime_count
    
    # numbers에 사용된 숫자들의 빈도를 계산하여 저장한 remaining
    remaining = [[int(k), v] for k, v in Counter(numbers).items()]
    result = BFS(0, 0, remaining)
    return len(result)  # set의 길이를 반환하도록 수정
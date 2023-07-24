import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(arr):
    while len(arr) != 2:
        result = []
        for i in range(len(arr) - 1):
            result.append(lcm(arr[i], arr[i+1]))
        arr = result
    answer = lcm(arr[0], arr[1])
    return answer
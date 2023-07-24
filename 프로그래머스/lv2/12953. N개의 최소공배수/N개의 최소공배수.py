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

# import math를 하면 math.lcm과 math.gcd 모두 사용가능한 것으로 알고 있는데 왜 안되는건지 몰라서 결국 lcm 함수를 직접 선언
# 두 수의 곱을 최대공약수로 나누면 최소공배수가 나온다.

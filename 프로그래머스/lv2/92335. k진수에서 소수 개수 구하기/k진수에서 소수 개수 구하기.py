def solution(n, k):
    lst = []
    # k진수로의 변환
    def convert(n, k):
        while True:
            if n == 0:
                break
            lst.append(n % k)
            n //= k
        return lst[::-1]
    result = convert(n, k)
    # 소수 판별 알고리즘
    def prime_number(x):
        if x == 0 or x == 1:
            return False
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True
    
    num = ""
    num_list = []
    for i in result:
        if i != 0:
            num += str(i)
        else:
            if len(num) == 0:
                continue
            else:   
                num_list.append(int(num))
                num = ""
    if len(num) > 0:
        num_list.append(int(num))
    
    answer = 0
    for i in num_list:
        if prime_number(i):
            answer += 1
    return answer
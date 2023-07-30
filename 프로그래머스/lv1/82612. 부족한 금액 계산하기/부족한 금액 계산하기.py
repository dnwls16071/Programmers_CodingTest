def solution(price, money, count):
    answer = -1
    result = 0
    for i in range(1, count+1):    
        result += price * i
    if result >= money:
        return abs(result - money)
    else:
        return 0
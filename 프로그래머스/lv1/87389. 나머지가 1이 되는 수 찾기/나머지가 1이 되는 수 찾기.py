def solution(n):
    x = 1
    while True:
        if n % x == 1:
            break
        x += 1
    return x
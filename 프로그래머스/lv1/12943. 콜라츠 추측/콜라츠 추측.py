def solution(num):
    cnt = 0
    return recursive(num, cnt)

def recursive(num, cnt):
    if num == 1:
        return cnt
    if cnt == 500:
        return -1
    
    if num % 2 == 0:
        return recursive(num // 2, cnt + 1)
    else:
        return recursive(num * 3 + 1, cnt + 1)
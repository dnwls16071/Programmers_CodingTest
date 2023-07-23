def solution(a, b):
    
    a = str(a)
    b = str(b)
    res1 = int(a + b)
    res2 = int(b + a)
    if res1 >= res2:
        return res1
    else:
        return res2
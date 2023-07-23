def solution(a, d, included):
    result = 0
    
    # 인덱스, 값을 받아오는 함수인 enumerate를 사용함
    for idx, val in enumerate(included):
        if included[idx]:
            result += a + (idx * d)
            
    return result
def solution(dots):
    # 두 직선이 평행이 된다. → 두 직선의 기울기가 같아야 한다.
    answer = 0
    
    if abs(dots[0][1] - dots[1][1]) / abs(dots[0][0] - dots[1][0]) == abs(dots[2][1] - dots[3][1]) / abs(dots[2][0] - dots[3][0]):
        return 1
    elif abs(dots[0][1] - dots[2][1]) / abs(dots[0][0] - dots[2][0]) == abs(dots[1][1] - dots[3][1]) / abs(dots[1][0] - dots[3][0]):
        return 1
    elif abs(dots[0][1] - dots[3][1]) / abs(dots[0][0] - dots[3][0]) == abs(dots[1][1] - dots[2][1]) / abs(dots[1][0] - dots[2][0]):
        return 1
    else:
        return 0

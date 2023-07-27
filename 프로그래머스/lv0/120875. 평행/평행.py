def solution(dots):
    # 두 직선이 평행이 된다. → 두 직선의 기울기가 같아야 한다.
    answer = 0
    
    # 직선의 기울기 값이 항상 정수라고 보장할 수 없다.
    # 직선의 기울기 값이 소수인 경우도 나올 수 있기 때문에 이는 형변환을 하면 안됨
    # 따라서 몫을 구하는 연산자인 (//)을 사용하지 않고 실수 형태로 값이 반환되는 (/) 연산자를 사용해야함
    if abs(dots[0][1] - dots[1][1]) / abs(dots[0][0] - dots[1][0]) == abs(dots[2][1] - dots[3][1]) / abs(dots[2][0] - dots[3][0]):
        return 1
    elif abs(dots[0][1] - dots[2][1]) / abs(dots[0][0] - dots[2][0]) == abs(dots[1][1] - dots[3][1]) / abs(dots[1][0] - dots[3][0]):
        return 1
    elif abs(dots[0][1] - dots[3][1]) / abs(dots[0][0] - dots[3][0]) == abs(dots[1][1] - dots[2][1]) / abs(dots[1][0] - dots[2][0]):
        return 1
    else:
        return 0

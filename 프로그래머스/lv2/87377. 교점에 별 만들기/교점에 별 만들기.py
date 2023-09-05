# 1000개의 직선의 개수
# 직선이 겹쳐서 교점이 무한히 발생하지 않는다. → O(N^2)
# 1000 × 1000 크기 이내에서 표현됨
# INF값을 int 범위를 넘어서 주면 해결 → 1e15정도
def solution(line):
    # 교점을 저장할 리스트인 dot_list
    max_x = -int(1e15)
    min_x = int(1e15)
    max_y = -int(1e15)
    min_y = int(1e15)
    dot_list = []
    for i in range(len(line)):
        a, b, c = line[i]
        for j in range(i+1, len(line)):
            d, e, f = line[j]
            # 두 직선의 기울기가 같은 경우 : 교점이 발생할 수 없음
            if a * e == b * d:
                continue
            # 교점이 발생하는 경우 : 각각의 교점을 계산
            else:
                # Ax + By + C = 0
                # Dx + Ey + F = 0
                x = (b * f - c * e) / (a * e - b * d)
                y = (a * f - c * d) / (b * d - a * e)
            
            # 교점이 정수인 것만 취함
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                dot_list.append([x, y])
                # x축의 최대 범위와 y축의 최대 범위를 설정
                if max_x < x:
                    max_x = x
                if max_y < y:
                    max_y = y
                if min_x > x:
                    min_x = x
                if min_y > y:
                    min_y = y
    # x축의 음수 ~ 양수까지의 가로 길이
    x_range = max_x - min_x + 1
    # y축의 음수 ~ 양수까지의 세로 길이
    y_range = max_y - min_y + 1
    # 2차원 배열 선언
    matrix = [['.'] * x_range for _ in range(y_range)]
    
    for x, y in dot_list:
        if min_x < 0:
            nx = x + abs(min_x)
        else:
            nx = x - min_x
        
        if min_y < 0:
            ny = y + abs(min_y)
        else:
            ny = y - min_y
        matrix[ny][nx] = '*'
    
    answer = []
    for i in matrix:
        answer.append(''.join(i))
    return answer[::-1]
# 문제 그대로 시계방향으로 회전을 하게 되면 숫자가 하나 사라지게 되는 문제가 발생한다.
# 14, 20, 26
# 27, 28
# 10, 16, 22
# 8, 9
def rotate(x1, y1, x2, y2, matrix):
    # 초기값
    first = matrix[x1][y1]
    tmp = first
    
    for k in range(x1, x2):
        matrix[k][y1] = matrix[k+1][y1]
        tmp = min(tmp, matrix[k+1][y1])
    for k in range(y1, y2):
        matrix[x2][k] = matrix[x2][k+1]
        tmp = min(tmp, matrix[x2][k+1])
    for k in range(x2, x1, -1):
        matrix[k][y2] = matrix[k-1][y2]
        tmp = min(tmp, matrix[k-1][y2])
    for k in range(y2, y1+1, -1):
        matrix[x1][k] = matrix[x1][k-1]
        tmp = min(tmp, matrix[x1][k-1])
    matrix[x1][y1+1] = first
    return tmp

def solution(rows, columns, queries):
    answer = []
    num = 1
    # 2차원 배열을 생성
    matrix = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = num
            num += 1
    
    # queries에 따른 회전 실행
    for query in queries:
        x1, y1, x2, y2 = query
        ans = rotate(x1-1, y1-1, x2-1, y2-1, matrix)
        answer.append(ans)
    return answer
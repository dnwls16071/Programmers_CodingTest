def solution(ineq, eq, n, m):
    answer = 0
    
    # 각 조건을 따지는게 좀 귀찮았던 문제
    if (ineq == '>' and eq == '='):
        if n >= m :
            return 1 
        else:
            return 0
    elif (ineq == '<' and eq == '='):
        if n <= m:
            return 1
        else:
            return 0
    elif (ineq == '>' and eq == '!'):
        if n > m:
            return 1
        else:
            return 0
    elif (ineq == '<' and eq == '!'):
        if n < m:
            return 1
        else:
            return 0
    
    return answer
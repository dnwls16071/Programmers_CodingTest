def solution(sizes):
    # 명함들을 수납하는데 가로로 눕혀 수납하든 문제에서 준 조건으로 수납하든 수납만 되면 되기 때문에
    width = []      # 가로 길이, 세로 길이 중에서 큰 길이를 가로로 오도록
    height = []     # 가로 길이, 세로 길이 중에서 작은 길이를 세로로 오도록
    for size in sizes:
        Max = max(size)
        Min = min(size)
        width.append(Max)
        height.append(Min)
        
    Max_width = max(width)
    Max_height = max(height)
    tot = Max_width * Max_height
    return tot
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    # 한 변의 길이를 i로 가정
    for i in range(2, total):
        # 나머지 다른 변의 길이를 total // i로 가정
        side = total // i
        # 그림과 같이 노란색 블록이 껴있어야 하는 구조이기 때문에 가로, 세로 -2를 처리해준 다음 곱할 때 yellow 개수와 같다면?
        if (i - 2) * (side - 2) == yellow:
            answer = [i, side]
    return answer
# 시작 기둥에서 도착 기둥으로 이동
def hanoi(n, start, end, answer):
    if n == 1:
        return answer.append([start, end])
    # n-1개의 원반을 start에서 mid로 옮기고 가장 큰 원반만 end로 옮긴다.
    hanoi(n-1, start, 6-start-end, answer)
    # 맨 마지막에 있는 원반을 start에서 end로 옮긴다.
    answer.append([start, end])
    # mid에 있는 n-1개의 원반을 end로 옮긴다.
    hanoi(n-1, 6-start-end, end, answer)

def solution(n):
    answer = []
    hanoi(n, 1, 3, answer)
    return answer
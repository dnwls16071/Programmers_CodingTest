# 삼각형의 결정 조건 : 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야한다.
# 고려조건1. 가장 긴 변의 길이가 sides 배열 안에 존재하는 경우
# 고려조건2. 가장 긴 변의 길이가 나머지 한 변인 경우

def solution(sides):
    Min = min(sides)
    answer = 2 * Min - 1
    return answer
def solution(food):
    answer = ''
    # food 0번째 인덱싱 원소는 물에 해당됨
    water = food[0]
    # 절반만 탐색한 후 팰린드롬 문자열의 특성을 이용해 나머지 반쪽을 채움
    for i in range(1, len(food)):
        if food[i] // 2 >= 1:
            answer += str(i) * (food[i] // 2)
        else:
            continue
    result = answer + '0' + answer[::-1]
    return result
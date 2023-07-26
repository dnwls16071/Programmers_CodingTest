def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    answer = {}
    # 참가자 중에는 동명이인이 있을 수 있으므로 만약 동명이인이 존재한다면 value값을 1만큼 증가
    for val in participant:
        if val not in answer:
            answer[val] = 1
        else:
            answer[val] += 1
    
    # 완주자 명단을 받아와 만약 참가자 명단에 존재한다면 1만큼 감소(동명이인을 제외한 나머지 참가자들은 0이 됨)
    for i in completion:
        if i in answer:
            answer[i] -= 1
            
    # 딕셔너리의 Key와 Value를 모두 받아오는데 이 때 Value 값이 0이 아닌 Key, 즉 완주하지 못한 선수의 이름을 출력하기 위한 코드
    result = {key: value for key, value in answer.items() if value != 0}
    return list(result.keys())[0]
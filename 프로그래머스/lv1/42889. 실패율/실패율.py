def solution(N, stages):
    # N : 전체 스테이지의 개수
    # stages : 게임을 이용하는 사용자가 현재 멈춰 있는 스테이지의 번호가 담긴 배열
    answer = []
    users = len(stages)   # 전체 참가자 수
    stage_count = [0] * (N + 2) # 전체 스테이지의 개수 > 런타임에러가 발생한 이유
    # 각 스테이지에 도달한 사람의 수
    for i in stages:
        stage_count[i] += 1
    
    for i in range(1, N+1):
    # 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율 : 0
        if users == 0:
            failure_rate = 0
        else:
            failure_rate = stage_count[i] / users
    
        answer.append([i, failure_rate])
        users -= stage_count[i]
    
    # 정렬 1순위 : 실패율 내림차순
    # 정렬 2순위 : 스테이지 번호 오름차순
    answer.sort(key=lambda x : (-x[1], x[0]))
    answer = [x[0] for x in answer]
    return answer


# 시간초과 풀이(TLE) - 2중 반복문이 원인
def solution(N, stages):
    # N : 전체 스테이지의 개수
    # stages : 게임을 이용하는 사용자가 현재 멈춰 있는 스테이지의 번호가 담긴 배열
    temp = []
    participant = len(stages)   # 전체 참가자 수
    
    # 스테이지의 번호
    num = 1
    checked = [False] * (participant + 1)   # 스테이지를 탈락했는지 성공했는지를 확인하기 위한 변수
    for i in range(1, N+1): # 1 ~ N번 스테이지까지 총 N개의 스테이지가 존재
        challenge = 0 # 도전자 수
        failure = 0 # 조건을 충족하는 변수 저장 즉, X명의 사용자가 아직 클리어하지 못한 것인지를 확인하는 변수
        for j in range(participant):
            if stages[j] >= i and not checked[j]:
                challenge += 1
            if stages[j] == i and not checked[j]:
                failure += 1
                checked[j] = True
        if challenge == 0:
            failure_rate = 0
        else:
            failure_rate = failure / challenge
        result = [num, failure_rate]
        temp.append(result)
        num += 1
    
    # 정렬 1순위 : 실패율 내림차순
    # 정렬 2순위 : 스테이지 번호 오름차순
    answer = sorted(temp, key = lambda x : (-x[1], x[0]))
    result = [x[0] for x in answer]
    return result

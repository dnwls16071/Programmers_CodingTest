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
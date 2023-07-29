# 소요시간 : 1h 43m
# Lv1이지만 테스트케이스 3, 9번 시간초과 발생으로 많은 시간이 소요됨
def solution(id_list, report, k):
    # 동일한 유저에 대한 신고 횟수는 1회로 처리됨
    report = list(set(report))
    # 메일 발송 배열
    answer = [0] * len(id_list)
    # k번 이상 신고당한 경우 게시판 이용 불가
    dictionary = {id : 0 for id in id_list}
    # 각 유저별로 신고한 아이디와 정지된 아이디
    report_info = {id : [] for id in id_list}
    
    for i in report:
        userID, reportedID = i.split(" ")
        dictionary[reportedID] += 1
        report_info[userID].append(reportedID)
    
    # k번 이상 신고당한 유저의 경우 -> 일단 게시판 이용 불가함 
    for key, value in dictionary.items():
        if value >= k:
            # 각 사용자가 만약 k번 이상 신고당한 유저를 신고한 이력이 있다면?
            for user_id, reported_id in report_info.items():
                if key in reported_id:
                    # 각 사용자에게 메일 1개 발송
                    answer[id_list.index(user_id)] += 1
    return answer
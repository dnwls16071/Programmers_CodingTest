def solution(id_list, report, k):
    report = list(set(report))
    answer = [0] * len(id_list)
    dictionary = {id : 0 for id in id_list}
    report_info = {id : [] for id in id_list}
    
    for i in report:
        userID, reportedID = i.split(" ")
        dictionary[reportedID] += 1
        report_info[userID].append(reportedID)
    
    for key, value in dictionary.items():
        if value >= k:
            for user_id, reported_id in report_info.items():
                if key in reported_id:
                    answer[id_list.index(user_id)] += 1
    return answer
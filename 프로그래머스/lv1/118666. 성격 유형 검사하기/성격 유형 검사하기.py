def solution(survey, choices):
    answer = ''
    # 1번 지표 → 2번 지표 → 3번 지표 → 4번 지표
    my_dict = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0}
    for i in range(len(survey)):
        left_pt = survey[i][0]
        right_pt = survey[i][1]
        # 매우 비동의
        if choices[i] == 1:
            my_dict[left_pt] += 3
        # 비동의
        elif choices[i] == 2:
            my_dict[left_pt] += 2
        # 약간 비동의
        elif choices[i] == 3:
            my_dict[left_pt] += 1
        # 모르겠음
        elif choices[i] == 4:
            continue
        # 약간 동의
        elif choices[i] == 5:
            my_dict[right_pt] += 1
        # 동의    
        elif choices[i] == 6:
            my_dict[right_pt] += 2
        # 매우 동의
        elif choices[i] == 7:
            my_dict[right_pt] += 3
        
    # 1번 지표 비교
    if my_dict["R"] >= my_dict["T"]:
        answer += "R"
    else:
        answer += "T"
        
    # 2번 지표 비교
    if my_dict["C"] >= my_dict["F"]:
        answer += "C"
    else:
        answer += "F"
        
    # 3번 지표 비교
    if my_dict["J"] >= my_dict["M"]:
        answer += "J"
    else:
        answer += "M"
        
    # 4번 지표 비교
    if my_dict["A"] >= my_dict["N"]:
        answer += "A"
    else:
        answer += "N"
    return answer
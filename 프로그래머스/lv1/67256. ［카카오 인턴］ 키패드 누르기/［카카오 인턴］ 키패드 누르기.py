def solution(numbers, hand):
    answer = ''
    # 키패드의 각각의 위치를 좌표로 표현
    dic = {"1" : [0, 0], "2" : [0, 1], "3" : [0, 2],
           "4" : [1, 0], "5" : [1, 1], "6" : [1, 2],
           "7" : [2, 0], "8" : [2, 1], "9" : [2, 2],
           "*" : [3, 0], "0" : [3, 1], "#" : [3, 2]}
    
    # 현재 왼손 엄지손가락의 위치
    left_hand = "*"
    # 현재 오른손 엄지손가락의 위치
    right_hand = "#"
    
    for i in numbers:
        i = str(i)
        # 만약 키패드의 누른 위치가 [1, 4, 7, *]인 경우 → 왼손으로 터치
        if i in ["1", "4", "7"]:
            left_hand = i
            answer += "L"
        # 만약 키패드의 누른 위치가 [3, 6, 9, #]인 경우 → 오른손으로 터치
        elif i in ["3", "6", "9"]:
            right_hand = i
            answer += "R"
        # 만약 키패드의 누른 위치가 [2, 5, 8, 0]인 경우 → 키패드의 누른 위치와 각각의 엄지손가락의 위치를 계산
        else:
            left_hand_distance = abs(dic[i][0] - dic[left_hand][0]) + abs(dic[i][1] - dic[left_hand][1])
            right_hand_distance = abs(dic[i][0] - dic[right_hand][0]) + abs(dic[i][1] - dic[right_hand][1])
            
            # 만약 거리가 같으면? → hand에 따른 결과 처리
            if left_hand_distance == right_hand_distance:
                if hand == "left":
                    left_hand = i
                    answer += "L"
                else:
                    right_hand = i
                    answer += "R"
            # 만약 왼손과의 거리가 더 길면? → 오른손 엄지손가락으로 터치
            elif left_hand_distance > right_hand_distance:
                right_hand = i
                answer += "R"
            # 만약 오른손과의 거리가 더 길면? → 왼손 엄지손가락으로 터치
            else:
                left_hand = i
                answer += "L"
    return answer
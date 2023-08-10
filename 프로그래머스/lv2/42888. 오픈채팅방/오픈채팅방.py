# 문제를 보게 되면 Change의 경우 Change 명령어가 나오기 전 채팅방에 들어있는 사용자들의 정보도 갱신을 해줘야한다.
# Leave를 실행시켜 바로 제거하지않고 Change만 사용해서 바뀐 정보가 갱신이 되도록 작성한다.
# 그 다음 모든 정보를 갱신했다면 명령의 길이와 명령어 타입에 따라서 어떤 식으로 메시지를 출력할 것인지를 배열에 저장해야한다.

def solution(record):
    answer = []         # 최종적으로 방을 개설한 사람이 보게 되는 메시지
    curr_dict = {}      # 현재 사용자들을 저장한 딕셔너리
    for command in record:
        command = list(command.split(" "))
        if command[0] == "Enter":               
            curr_dict[command[1]] = command[2]
        elif command[0] == "Change":
            curr_dict[command[1]] = command[2]
    
    for command in record:
        command = list(command.split(" "))
        if len(command) >= 3:       # Enter와 Change의 경우(하지만 Change는 위에서 반영했으므로 Enter만 처리)
            command[2] = curr_dict[command[1]]
            if command[0] == "Enter":
                answer.append(str(command[2]) + "님이 들어왔습니다.")
        else:                       # 명령의 길이가 3미만인 경우 즉, Leave의 경우가 해당
            ID = curr_dict[command[1]]
            if command[0] == "Leave":
                answer.append(str(ID) + "님이 나갔습니다.")
    return answer
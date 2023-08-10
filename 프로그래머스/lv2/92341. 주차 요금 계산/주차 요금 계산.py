def solution(fees, records):
    answer = []
    my_dict = {}   # 차량 정보를 저장할 딕셔너리
    fee_dict = {}  # 주차 요금을 저장할 딕셔너리

    for record in records:
        prefix_time = 0
        record = record.split(" ")
        time = record[0]  # 시간
        temp = time.split(":")
        hour = int(temp[0])  # 시
        minute = int(temp[1])  # 분
        vehicle_number = record[1]  # 차량번호
        flag = record[2]  # 차량의 입차/출차 여부

        if flag == "IN":
            my_dict[vehicle_number] = [hour, minute]
        else:
            temp_hour = my_dict[vehicle_number][0]
            temp_minute = my_dict[vehicle_number][1]
            prefix_time = (hour - temp_hour) * 60 + (minute - temp_minute)
            if vehicle_number not in fee_dict:
                fee_dict[vehicle_number] = 0
            fee_dict[vehicle_number] += prefix_time
            del my_dict[vehicle_number]

    for vehicle_number, parked_time in my_dict.items():
        prefix_time = (
            (23 - parked_time[0]) * 60 + (59 - parked_time[1])
        )  # 남은 시간 계산
        if vehicle_number not in fee_dict:
            fee_dict[vehicle_number] = 0
        fee_dict[vehicle_number] += prefix_time

    for vehicle_number, total_time in fee_dict.items():
        if total_time <= fees[0]:
            result = fees[1]
        else:
            result = fees[1] + ((total_time - fees[0]) // fees[2] + int((total_time - fees[0]) % fees[2] != 0)) * fees[3]
        answer.append([vehicle_number, result])
    answer = sorted(answer, key = lambda x : int(x[0]))
    res = [answer[i][1] for i in range(len(answer))]
    return res
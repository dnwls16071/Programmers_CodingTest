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

        # 차량 입차의 경우 : 입차한 시간과 분을 저장
        if flag == "IN":
            my_dict[vehicle_number] = [hour, minute]
        # 차량 출차의 경우 : 출차한 시간과 분을 temp_hour, temp_minute 변수에 저장
        else:
            temp_hour = my_dict[vehicle_number][0]
            temp_minute = my_dict[vehicle_number][1]
            # 주차한 시간을 계산
            prefix_time = (hour - temp_hour) * 60 + (minute - temp_minute)
            # 주차 요금 저장 딕셔너리에 해당 차량 정보가 없는 경우라면?
            if vehicle_number not in fee_dict:
                fee_dict[vehicle_number] = 0
            # 있다면 주차한 시간만큼 값을 더해줌
            fee_dict[vehicle_number] += prefix_time
            # 출차했으므로 차량 정보를 저장하는 딕셔너리에서는 삭제
            del my_dict[vehicle_number]

    # 입차해놓고 23:59까지 출차를 하지 않았을 경우에 대한 주차 시간도 계산을 해줘야함
    for vehicle_number, parked_time in my_dict.items():
        prefix_time = ((23 - parked_time[0]) * 60 + (59 - parked_time[1]))
        if vehicle_number not in fee_dict:
            fee_dict[vehicle_number] = 0
        fee_dict[vehicle_number] += prefix_time

    # 주차 요금을 계산 : 기본 요금 + ((주차한 시간 - 기본 시간) / 단위시간) × 단위요금
    for vehicle_number, total_time in fee_dict.items():
        # 기본 시간보다 낮은 시간동안 주차했다면? : 그냥 기본 요금
        if total_time <= fees[0]:
            result = fees[1]
        # 아니라면? : 위에 공식처럼 계산을 적용
        else:
            result = fees[1] + ((total_time - fees[0]) // fees[2] + int((total_time - fees[0]) % fees[2] != 0)) * fees[3]
        # "차량 번호가 작은 자동차부터" 람다 정렬을 수행하기 위해 배열에 [차량 번호, 청구 금액] 순서로 저장
        answer.append([vehicle_number, result])
    # "차량 번호가 작은 자동차부터" 람다 정렬을 수행(문자열이므로 정수형으로 변환)
    answer = sorted(answer, key = lambda x : int(x[0]))
    # 필요한 것은 청구 금액이므로 아래와 같이 리스트 컴프리헨션을 이용해서 깔끔하게 코드를 작성 후 리턴
    res = [answer[i][1] for i in range(len(answer))]
    return res
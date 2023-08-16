def solution(files):
    answer = []
    for file in files:
        head = ""
        number = ""
        tail = ""
        flag = False
        for i in range(len(file)):
            # 숫자인 경우 : NUMBER → HEAD에 들어가지 않음
            if file[i].isdigit():
                number += file[i]
                flag = True
            # flag : False인 경우 
            elif not flag:
                head += file[i]
            else:
                tail = file[i:]
                break
        answer.append([head, number, tail])
    # answer 다중 정렬 수행
    # 첫 번째 우선순위 정렬 : 파일명은 우선 HEAD 부분을 기준으로 사전 순으로 정렬한다.(문자열 비교 시 대소문자 구분을 안하므로 소문자 임시 변환 후에 정렬을 수행)
    # 두 번째 우선순위 정렬 : NUMBER의 숫자 순으로 정렬(숫자 앞의 0은 무시 : int형으로 변환)
    answer = sorted(answer, key = lambda x : (x[0].lower(), int(x[1])))
    return [''.join(i) for i in answer]
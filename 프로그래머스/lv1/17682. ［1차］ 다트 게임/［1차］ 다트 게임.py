def solution(dartResult):
    lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    res = ""
    answer = 0
    result = []
    
    for i in dartResult:
        # 입력받은 값이 정수인 경우 → 문자열 추가(ex. 두 자리의 경우 처리를 위해서)
        if i in lst:
            res += i
        # 보너스가 S인 경우 → 1제곱 수행
        elif i == "S":
            res = int(res) ** 1
            result.append(res)
            res = ""
        # 보너스가 D인 경우 → 2제곱 수행
        elif i == "D":
            res = int(res) ** 2
            result.append(res)
            res = ""
        # 보너스가 T인 경우 → 3제곱 수행
        elif i == "T":
            res = int(res) ** 3
            result.append(res)
            res = ""
        # 옵션이 스타상인 경우 → 점수의 2배(하지만 스타상의 효과는 중첩이 가능하므로 이를 분기문으로 해결)
        elif i == "*":
            if len(result) > 1:
                result[-2] = result[-2] * 2
                result[-1] = result[-1] * 2
            else:
                result[-1] = result[-1] * 2
        # 옵션이 아차상인 경우 → 점수 × (-1)
        elif i == "#":
            result[-1] = result[-1] * (-1)
    return sum(result)
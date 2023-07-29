# 1
# 데이터의 개수를 셀 때 유용한 파이썬의 collections 모듈의 Counter 클래스
from collections import Counter

def solution(X, Y):
    # 아래와 같은 코드로 작성을 하게 되면 딕셔너리 형태로 지원
    # 각 원소가 몇 번의 빈도값을 가지는지 저장된 객체를 얻을 수 있다.
    X_dict = Counter(X)
    Y_dict = Counter(Y)
    
    # 교집합을 구하는 방법
    intersection = list((X_dict & Y_dict).elements())
    if len(intersection) == 0:
        return "-1"
    else:
        result = list(intersection)
    if int(''.join(map(str, result))) == 0:
        return "0"
    else:
        result = sorted(result, reverse=True)
        return ''.join(map(str, result))

#2
# 데이터의 개수를 셀 때 유용한 파이썬의 collections 모듈의 Counter 클래스
from collections import Counter

def solution(X, Y):
    # 아래와 같은 코드로 작성을 하게 되면 딕셔너리 형태로 지원
    # 각 원소가 몇 번의 빈도값을 가지는지 저장된 객체를 얻을 수 있다.
    X_dict = Counter(X)
    Y_dict = Counter(Y)
    result = []
    
    # 교집합을 구하는 방법 -> 구하고자 하는 것은 X와 Y에 등장하는 숫자 중에서 중복되는 숫자
    intersection = set((X_dict & Y_dict).elements())
    for num in intersection:
        count_X_dict = X_dict[num]
        count_Y_dict = Y_dict[num]
        if count_X_dict > 0 and count_Y_dict > 0:
            # 두 문자열 X와 Y에서 해당 숫자 num의 등장 횟수의 최소값만큼을 리스트에 extend시킴
            # append가 아닌 이유 : [테스트케이스 5번 예시]
            Min = min(count_X_dict, count_Y_dict)
            result.extend(num * Min)
    
    if not result:
        return "-1"
    else:
        result = sorted(result, reverse=True)
        # [테스트케이스 2번 예시] -> "0000" -> "0"으로 리턴
        return str(int(''.join(map(str, result))))

# 3    
# 데이터의 개수를 셀 때 유용한 파이썬의 collections 모듈의 Counter 클래스
from collections import Counter

def solution(X, Y):
    answer = ""
    # 아래와 같은 코드로 작성을 하게 되면 딕셔너리 형태로 지원
    # 각 원소가 몇 번의 빈도값을 가지는지 저장된 객체를 얻을 수 있다.
    X_dict = Counter(X)
    Y_dict = Counter(Y)
    result = []
    
    # 교집합을 구하는 방법 -> 구하고자 하는 것은 X와 Y에 등장하는 숫자 중에서 중복되는 숫자
    intersection = list(set((X_dict & Y_dict).elements()))
    if not intersection:
        return "-1"
    elif intersection == ["0"]:
        return "0"
    else:
        intersection = sorted(intersection, reverse=True)
        for num in intersection:
            Min = min(X_dict[num], Y_dict[num])
            answer += num * Min
        return answer
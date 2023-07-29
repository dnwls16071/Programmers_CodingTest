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
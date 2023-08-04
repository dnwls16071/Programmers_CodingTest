from collections import Counter

def solution(clothes):
    answer = 1
    my_dict = Counter(x[1] for x in clothes)
    
    # i + 1 이유 : 각 의상을 선택하지 않았을 경우를 고려
    for i in my_dict.values():
        answer *= (i+1)
    # 하루에 최소 한 개의 의상은 입기 때문에 하나도 안 입은 경우는 제외
    answer -= 1
    return answer
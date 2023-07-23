def solution(strArr):
    answer = 0
    my_dict = {}
    for i in strArr:
        if len(i) not in my_dict:
            my_dict[len(i)] = 1
        else:
            my_dict[len(i)] += 1
    # 딕셔너리 자료구조와 람다 정렬을 활용한 방법을 이용
    lst = sorted(my_dict.items(), key = lambda x : -x[1])
    return lst[0][1]
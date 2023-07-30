from collections import defaultdict
def solution(X, Y):
    answer = ""
    x_dict = defaultdict(int)
    y_dict = defaultdict(int)
    for i in X:
        x_dict[i] += 1
    for i in Y:
        y_dict[i] += 1

    intersection = list(set((x_dict.keys() & y_dict.keys())))
    if not intersection:
        return "-1"
    elif intersection == ["0"]:
        return "0"
    else:
        intersection = sorted(intersection, reverse=True)
        for num in intersection:
            Min = min(x_dict[num], y_dict[num])
            answer += num * Min
        return answer
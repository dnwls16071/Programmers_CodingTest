def solution(s):
    s = list(map(int, s.split(" ")))
    Min = min(s)
    Max = max(s)
    answer = [Min, Max]
    return ' '.join(map(str, answer))
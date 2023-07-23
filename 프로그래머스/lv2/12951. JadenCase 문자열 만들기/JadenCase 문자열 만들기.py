def solution(s):
    answer = ''
    
    s = s.split(" ")
    for idx, val in enumerate(s):
        s[idx] = s[idx][:1].upper() + s[idx][1:].lower()
    return ' '.join(s)

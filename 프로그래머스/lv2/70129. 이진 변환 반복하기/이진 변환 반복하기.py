def solution(s):
    answer = []
    # 제거할 0의 개수
    cnt = 0
    # 회차 카운팅
    temp = 0
    
    while s != "1":
        zero_cnt = s.count("0")
        cnt += zero_cnt
        changed_num = len(s) - zero_cnt
        s = bin(changed_num)[2:]
        temp += 1        
    return [temp, cnt]
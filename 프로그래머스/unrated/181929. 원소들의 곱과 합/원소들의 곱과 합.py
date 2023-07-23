def solution(num_list):
    answer1 = 1
    answer2 = 0
    
    # 모든 원소들의 곱
    for i in num_list:
        answer1 *= i
    
    # 모든 원소들의 합의 제곱
    for i in num_list:
        answer2 += i
    answer2 = answer2 ** 2 
        
    if answer1 < answer2:
        return 1
    elif answer1 > answer2:
        return 0
def solution(num_list):
    even = ""
    odd = ""
    
    # odd : 홀수, even : 짝수
    for i in num_list:
        if i % 2 != 0:
            odd += str(i)
        else:
            even += str(i)
    
    odd = int(odd)
    even = int(even)
    return odd + even
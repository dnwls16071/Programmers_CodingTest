def solution(str1, str2):
    answer = ''
    
    str1 = list(str1)
    str2 = list(str2)
    
    # 여러 객체를 하나로 묶어주는 기능을 수행하는 zip 함수를 사용
    for i in zip(str1, str2):
        # tuple 형태로 반환되므로 이를 문자열로 변환해주는 join 함수를 사용
        tmp = str(''.join(map(str, i)))
        answer += tmp
    return answer
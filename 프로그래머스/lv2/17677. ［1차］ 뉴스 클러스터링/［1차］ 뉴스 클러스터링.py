import itertools

def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)
    
def solution(str1, str2):
    # 대문자와 소문자의 차이는 무시하므로 소문자로 통일
    str1 = str1.lower()
    str2 = str2.lower()
    
    # itertools 모듈의 pairwise를 정의한 후 사용 → 문자열 두 글자씩 묶어서 다중집합의 원소로 만드는 메소드
    str1_pair = pairwise(str1)
    str2_pair = pairwise(str2)
    
    str1_lst = []
    str2_lst = []
    for i in str1_pair:
        temp = ''.join(map(str, i))
        # 문자열이 문자열이면서 길이가 2인 경우(즉, 길이가 2가 아닌 경우는 공백을 포함하고 있다는 뜻이 되므로)
        if temp.isalpha() and len(temp) == 2:
            str1_lst.append(temp)
            
    for i in str2_pair:
        temp = ''.join(map(str, i))
        if temp.isalpha() and len(temp) == 2:
            str2_lst.append(temp)
    
    intersection = []       # 교집합
    union = []              # 합집합
    
    for item in str1_lst:
        if item in str2_lst:
            intersection.append(item)
            str2_lst.remove(item)
        union.append(item)
    union.extend(str2_lst)
    
    try:
        result = (len(intersection) / len(union)) * 65536
        return int(result)
    except ZeroDivisionError:           # 공집합이 0인 경우 즉, 교집합도 공집합도 존재하지 않는 경우 65536 반환(테스트케이스4)
        return 65536
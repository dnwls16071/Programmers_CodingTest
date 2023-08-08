def solution(s):
    # 문자열에서 괄호와 쉼표를 제거한 후 길이에 따라 정렬
    sorted_data = sorted(s[2:-2].split("},{"), key=lambda x: len(x.split(',')))

    # 정렬된 데이터를 다시 문자열 형태로 변환하여 출력
    s = "{{" + "},{".join(sorted_data) + "}}"
    
    s = s.replace('{','')
    s = s.replace('}','')
    s = list(s.split(','))
    s = list(map(int, s))
    
    result = []
    for i in s:
        if i not in result:
            result.append(i)
    return result
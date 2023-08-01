def solution(s, skip, index):
    # 알파벳 26문자 배열
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # 주어진 규칙대로 s를 변환한 결과를 저장할 문자열 변수 answer
    answer = ""
    for i in range(len(s)):
        # temp → index만큼 뒤에 있는 알파벳을 찾기 위한 변수
        temp = index
        # 시작점 인덱스 idx
        idx = alphabet.index(s[i])
        while temp != 0:
            # idx의 값이 26이상이라면? → IndexError 우려가 있으므로 나머지 연산으로 처리해줌
            if idx >= 26:
                idx %= 26
                # 만약 해당 인덱싱 문자가 skip 배열에 들어있는 문자라면?
                if alphabet[(idx + 1) % 26] in skip:
                    idx += 1
                # 만약 해당 인덱싱 문자가 skip 배열에 들어있지 않은 문자라면?
                else:
                    idx += 1
                    temp -= 1
            # idx의 값이 26미만이라면?
            else:
                if alphabet[(idx + 1) % 26] in skip:
                    idx += 1
                else:
                    idx += 1
                    temp -= 1
        answer += alphabet[idx % 26]
    return answer
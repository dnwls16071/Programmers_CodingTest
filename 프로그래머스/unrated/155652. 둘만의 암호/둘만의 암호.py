def solution(s, skip, index):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    answer = ""
    for i in range(len(s)):
        temp = index
        idx = alphabet.index(s[i])
        while temp != 0:
            if idx >= 26:
                idx %= 26
                if alphabet[(idx + 1) % 26] in skip:
                    idx += 1
                else:
                    idx += 1
                    temp -= 1
            else:
                if alphabet[(idx + 1) % 26] in skip:
                    idx += 1
                else:
                    idx += 1
                    temp -= 1
        answer += alphabet[idx % 26]
    return answer

def solution(n, words):
    answer = [0, 0]
    for i in range(1, len(words)):
        # 해당 단어가 이전에 불렸거나 다음 단어 앞 철자가 이전 단어 마지막 철자와 일치하지 않는 경우
        if words[i] in words[:i] or words[i][0] != words[i-1][-1]:
            answer[0] = i % n +1
            answer[1] = i // n +1
            return answer
    return [0, 0]
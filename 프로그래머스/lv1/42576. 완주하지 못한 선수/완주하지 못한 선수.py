def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    answer = {}
    for idx, val in enumerate(participant):
        if val not in answer:
            answer[val] = 1
        else:
            answer[val] += 1
            
    for i in completion:
        if i in answer:
            answer[i] -= 1
    
    result = {key: value for key, value in answer.items() if value != 0}
    return list(result.keys())[0]
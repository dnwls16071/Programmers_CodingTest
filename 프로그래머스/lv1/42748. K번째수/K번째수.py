def solution(array, commands):
    answer = []
    for command in commands:
        left = command[0]
        right = command[1]
        idx = command[2]
        temp = sorted(array[left-1:right])
        answer.append(temp[idx-1])
    return answer
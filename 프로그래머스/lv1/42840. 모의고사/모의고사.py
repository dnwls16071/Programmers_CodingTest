# 1) - [3, 3, 2, 1, 5] -> [3]
# 2) - [5, 5, 4, 2, 3] -> [1,2,3]

# 1) 문제 잘 읽어보면 최대값의 학생만 구하는 겁니다. 학생들이 몇개 맞췄는지 나열하는게 아니라
# 2) 수포자 3명 다 0문제 맞췄을 시 최대값은 0이고, 세명 다 최대값을 가지는 학생이고, 값이 같아서 오름차순 1,2,3 으로 출력

def solution(answers):
    ans_1 = [1, 2, 3, 4, 5]                 # 1번 수포자
    ans_2 = [2, 1, 2, 3, 2, 4, 2, 5]        # 2번 수포자
    ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 3번 수포자
    answer = [0, 0, 0]                      # 맞힌 문항을 나타내는 배열
    
    result = []
    for idx, value in enumerate(answers):
        if ans_1[idx % 5] == value:
            answer[0] += 1
        if ans_2[idx % 8] == value:
            answer[1] += 1
        if ans_3[idx % 10] == value:
            answer[2] += 1
    
    Max = max(answer)
    for i in range(len(answer)):
        if answer[i] == Max:
            result.append(i+1)
    return result
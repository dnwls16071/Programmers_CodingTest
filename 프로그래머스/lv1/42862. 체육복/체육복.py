def solution(n, lost, reserve):
    # 학생들의 체육복 소지 여부 상태
    students = [1] * (n + 1)

    # 체육복이 없는 학생은 -1
    for l in lost:
        students[l] -= 1

    # 여벌 체육복을 가진 학생은 +1을 해줘야함
    # 왜냐면 문제 조건에 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있다고 했기 때문에 자신의 체육복이 없어지면 다른 학생에게 체육복을 빌려줄 수 없음
    for r in reserve:
        students[r] += 1

    for i in range(1, n + 1):
        # 여벌 체육복이 있는 경우
        if students[i] == 2:  
            if i - 1 > 0 and students[i - 1] == 0: 
                students[i - 1] = 1
                students[i] = 1 
            elif i + 1 <= n and students[i + 1] == 0:  
                students[i + 1] = 1
                students[i] = 1

    answer = 0
    for i in range(1, n+1):
        if students[i] >= 1:
            answer += 1
    return answer

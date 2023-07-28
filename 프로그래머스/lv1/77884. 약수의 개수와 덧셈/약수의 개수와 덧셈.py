def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        temp = 0
        # 약수를 구하는 과정
        for j in range(1, i+1):
            if i % j == 0:
                temp += 1
        # 약수의 개수가 짝수개라면?
        if temp % 2 == 0:
            answer += i
        # 약수의 개수가 홀수개라면?
        else:
            answer -= i
    return answer
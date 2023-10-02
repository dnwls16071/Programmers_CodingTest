def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        time = 0
        for j in range(i, len(prices)-1):
            # 가격이 같거나 큰 경우
            if prices[i] <= prices[j]:
                time += 1
            else:
                break
        answer.append(time)
    # 마지막은 0초간 가격이 떨어지지 않으므로
    answer.append(0)
    return answer
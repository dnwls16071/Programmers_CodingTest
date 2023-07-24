def solution(players, callings):
    answer = players
    # 딕셔너리 자료구조를 이용해서 선수와 인덱스를 지정
    my_dict = {}
    for i,v in enumerate(players):
        my_dict[v] = i
        
    for call in callings:
        # 이전 선수와 해당 선수의 Swap과정이 수행
        previous, now = my_dict[call] - 1, my_dict[call]
        my_dict[players[previous]] = now
        my_dict[players[now]] = previous
        # players 배열을 복사한 answer 배열을 이용해 Swap 과정 수행
        answer[previous], answer[now] = answer[now], answer[previous]
    return answer
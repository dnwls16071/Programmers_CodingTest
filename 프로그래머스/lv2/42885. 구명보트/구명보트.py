# 한 구명보트에 탑승할 수 있는 인원의 수는 최대 2명
# 따라서 정렬을 수행한 후에 투 포인터를 이용해서 무게 제한을 넘기는지 넘기지 않는지를 판단하는 것이 중요
def solution(people, limit):
    answer = 0
    left = 0
    right = len(people) - 1
    people.sort()
    
    while left <= right:
        if people[left] + people[right] <= limit:
            answer += 1
            left += 1
            right -= 1
        elif people[left] + people[right] > limit:
            answer += 1
            right -= 1
    return answer
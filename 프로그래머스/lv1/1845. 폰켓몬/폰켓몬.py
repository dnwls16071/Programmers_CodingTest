def solution(nums):
    # 중복을 제거하여 유니크한 폰켓몬의 종류를 파악
    phoneketmon = list(set(nums))
    
    # 선택할 수 있는 최대 폰켓몬의 종류 수는 유니크한 폰켓몬 종류의 수와 N/2 중 작은 값
    max_phoneketmon = min(len(phoneketmon), len(nums) // 2)
    return max_phoneketmon

# 테스트케이스 제작
# [2, 2, 3, 3, 3, 3]
# 6마리의 폰켓몬 중에서 3마리의 폰켓몬을 선택

# [2, 2, 3] → 2종류의 폰켓몬 픽
# [2, 3, 3] → 2종류의 폰켓몬 픽
# [3, 3, 3] → 1종류의 폰켓몬 픽
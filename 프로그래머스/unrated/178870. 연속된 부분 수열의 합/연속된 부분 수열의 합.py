# 투 포인터와 누적 합을 이용하는 문제
def solution(sequence, k):
    n = len(sequence)
    left = 0
    right = -1
    curr = 0
    min_length = 1000001
    result = []
    
    while right <= n-1:
        if curr < k:
            right += 1
            if right >= n:
                break
            curr += sequence[right]
        else:
            curr -= sequence[left]
            if left >= n:
                break
            left += 1
            
        if curr == k:
            if min_length > right - left + 1:
                min_length = right - left + 1
                result = [left, right]

    return result
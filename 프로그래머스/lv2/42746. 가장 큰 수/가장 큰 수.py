def solution(numbers):
    answer = ''
    Max_length = len(str(max(numbers)))
    # 문자열 연산을 위해 문자로 취급
    arr = list(map(str, numbers))
    
    # 마지막 숫자를 numbers 배열의 최댓값의 길이만큼 동일하게 맞춰줌
    result = sorted(arr, key = lambda x : x * 3, reverse=True)
    # 테스트케이스 11번 반례 : [0, 0, 0, 0] → "0"
    if int(''.join(map(str, result))) == 0:
        return "0"
    else:
        return ''.join(map(str, result))

# 문제 접근법 
# 1) 각 원소의 자릿수를 동일하게 맞춰서 정렬을 수행       ( X )
# 2) 각 원소 문자열을 한 번 더 이어붙여 정렬을 수행       ( X )
# 3) 


# 테스트케이스1 → [6, 10, 2]
# [66, 10, 22] → [66, 22, 10] ▶ 따라서, 결과는 6210

# 테스트케이스2 → [3, 30, 34, 5, 9]
# [33, 30, 34, 55, 99] → [99, 55, 34, 33, 30] ▶ 따라서, 결과는 9534330
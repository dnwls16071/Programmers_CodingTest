def solution(numbers):
    answer = ''
    Max_length = len(str(max(numbers)))
    # 문자열 연산을 위해 문자로 취급
    arr = list(map(str, numbers))
    
    # 마지막 숫자를 numbers 배열의 최댓값의 길이만큼 동일하게 맞춰줌
    # numbers의 길이는 1 ≤ len(numbers) ≤ 100,000
    # numbers의 원소는 0 ≤ element ≤ 1,000
    result = sorted(arr, key = lambda x : x * 3, reverse=True)
    # 테스트케이스 11번 반례 : [0, 0, 0, 0] → "0"
    if int(''.join(map(str, result))) == 0:
        return "0"
    else:
        return ''.join(map(str, result))

# 문제 접근법 
# 1) 각 원소의 자릿수를 동일하게 맞춰서 정렬을 수행       ( X )
# 2) 각 원소 문자열을 한 번 더 이어붙여 정렬을 수행       ( X )
# 3) 문자열 × 3


# 테스트케이스1 → [6, 10, 2]
# ["666", "101010", "222"] → 원소의 값은 `숫자`가 아닌 `문자`이고 이를 내림차순 정렬하면 ["666", "222", "101010"] 
# 따라서 만들 수 있는 가장 큰 수는 6210
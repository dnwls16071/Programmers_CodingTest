# 리스트에서 최솟값을 찾는 min을 사용
def solution(arr, queries):
    answer = []
    temp = []
    for query in queries:
        left = query[0]
        right = query[1]
        k = query[2]
        for i in range(left, right+1):
            if arr[i] > k:
                temp.append(arr[i]) 
        if len(temp) == 0:
            answer.append(-1)
        else:
            answer.append(min(temp))
            temp = []
    return answer

# 기준이 되는 최솟값을 정해준 다음 비교하는 방식
def solution(arr, queries):
    answer = []
    for query in queries:
        left = query[0]
        right = query[1]
        k = query[2]
        
        # 쿼리마다 최소값을 찾기 위해 None으로 초기화 > 매우 중요함
        min_val = None
        
        for i in range(left, right+1):
            if arr[i] > k:  # 모든 i에 대해 k보다 크다
                if min_val is None or arr[i] < min_val:
                    min_val = arr[i]
        
        if min_val is not None:
            answer.append(min_val)
        else:
            answer.append(-1)
    return answer
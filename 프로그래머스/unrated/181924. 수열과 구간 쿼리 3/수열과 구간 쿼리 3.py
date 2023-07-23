def solution(arr, queries):
    answer = []
    
    for query in queries:
        left = query[0]
        right = query[1]
        arr[left], arr[right] = arr[right], arr[left]
    return arr
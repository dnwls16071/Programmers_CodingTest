def solution(arr, queries):
    for query in queries:
        left = query[0]
        right = query[1]
        k = query[2]
        for i in range(left, right+1):
            if i % k == 0:
                arr[i] += 1
    return arr
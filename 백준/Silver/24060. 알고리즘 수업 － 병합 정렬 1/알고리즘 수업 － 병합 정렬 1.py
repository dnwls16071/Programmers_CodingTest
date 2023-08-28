import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = (len(arr) + 1) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    i = 0
    j = 0
    tmp = []
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            tmp.append(left_arr[i])
            answer.append(left_arr[i])
            i += 1
        else:
            tmp.append(right_arr[j])
            answer.append(right_arr[j])
            j += 1

    while i < len(left_arr):
        tmp.append(left_arr[i])
        answer.append(left_arr[i])
        i += 1

    while j < len(right_arr):
        tmp.append(right_arr[j])
        answer.append(right_arr[j])
        j += 1

    return tmp

N, K = map(int, input().strip().split())
lst = list(map(int, input().strip().split()))
answer = []
merge_sort(lst)

if len(answer) >= K:
    print(answer[K-1])
else:
    print(-1)
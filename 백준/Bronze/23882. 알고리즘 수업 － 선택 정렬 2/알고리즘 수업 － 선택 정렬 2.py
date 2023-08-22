import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
array = list(map(int, input().strip().split()))
cnt = 0

def selection_sort(array):
    global cnt
    # 가장 큰 수 A[i]를 찾는다.
    for i in range(len(array) - 1, 0, -1):
        is_swapped = False
        max_index = i
        for j in range(i-1, -1, -1):
            if array[max_index] < array[j]:
                max_index = j
                is_swapped = True
        if max_index != i:
            array[i], array[max_index] = array[max_index], array[i]
            cnt += 1
        if cnt == K:
            print(*array)
            sys.exit(0)
    print(-1)

selection_sort(array)
def solution(my_string, queries):
    my_string = list(my_string)
    for query in queries:
        left = query[0]
        right = query[1]
        my_string[left:right+1] = my_string[left:right+1][::-1]
    result = str(''.join(map(str, my_string)))
    return result
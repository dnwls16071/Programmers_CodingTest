def binary_convert(n):
    binary_num = bin(n)[2:]
    return binary_num

def solution(n):
    answer = 0
    result = n + 1
    while True:
        res = binary_convert(n)
        res_one_cnt = res.count("1")
        
        binary_result = binary_convert(result)
        result_one_cnt = binary_result.count("1")
        
        if res_one_cnt == result_one_cnt:
            return result
        else:
            result += 1
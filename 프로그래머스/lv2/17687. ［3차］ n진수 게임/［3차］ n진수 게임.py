# num을 n진법으로
def convert(num, n):
    arr = ["A", "B", "C", "D", "E", "F"]
    result = ""
    if num == 0:
        return "0"
    while num != 0:
        # 나머지가 10 ~ 15인 경우 : 대문자 A ~ F로 출력
        if num % n >= 10:
            result += str(arr[(num % n) - 10])
        else:
            result += str(num % n)
        num //= n
    return result[::-1]

def solution(n, t, m, p):
    answer = ''
    game = ''
    # 미리 구할 숫자의 갯수 t × 게임에 참가하는 인원 m → 곱한 결과만큼 로테이션
    for num in range(t * m):
        game += convert(num, n)
    
    # p는 튜브의 순서
    for i in range(p-1, t*m, m):
        answer += game[i]
    return answer
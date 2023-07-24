import sys
input = sys.stdin.readline

N = int(input().strip())
guitar = []
for i in range(N):
    info = input().strip()
    len_info = len(info)
    val = 0
    for j in info:
        if j.isdigit():
            val += int(j)
    # 이름, 입력값 길이, 자릿수의 합
    guitar.append([info, len_info, val])

guitar = sorted(guitar, key = lambda x : (x[1], x[2], x[0]))
for i in range(len(guitar)):
    print(guitar[i][0])
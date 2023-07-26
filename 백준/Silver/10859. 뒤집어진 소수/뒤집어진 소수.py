import sys
input = sys.stdin.readline
def isPrime(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

N = int(input())
if N == 2 or N == 5:    # 2, 5는 뒤집혀서도 2, 5 그대로 소수이므로 yes
    print("yes")
    exit(0)
if '3' in str(N) or '4' in str(N) or '7' in str(N):     # 3, 4, 7은 뒤집히면 더 이상 숫자가 아니므로 no
    print("no")
    exit(0)
if isPrime(N):  # 입력값 N이 소수이면?
    t = list(str(N))[::-1]
    for i in range(len(t)):
        if t[i] == '6': # 6을 뒤집으면 9가 된다.
            t[i] = '9'
        elif t[i] == '9': # 9를 뒤집으면 6이 된다.
            t[i] = '6'
    t = int(''.join(t))
    if isPrime(t):  # 뒤집은 수 역시 소수이면?
        print("yes")
    else:           # 뒤집은 수가 소수가 아니라면?
        print("no")
else:   # 입력값 N이 소수가 아니라면?
    print("no")
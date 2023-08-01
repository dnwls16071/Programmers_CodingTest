import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = denom1 * denom2
    numer = numer1 * denom2 + numer2 * denom1
    # 최대공약수 1 → 두 수는 서로소의 관계가 성립됨
    if math.gcd(denom, numer) == 1:
        return [numer, denom]
    else:
        return [numer // math.gcd(denom, numer), denom // math.gcd(denom, numer)]
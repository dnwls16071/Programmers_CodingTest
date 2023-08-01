# 기약분수의 형태로 미리 나누지 않고 통분을 진행해서 공통분모를 같게 만듦
# 분모와 분자의 값이 서로소 관계면 기약분수 형태가 됨
# 분모와 분자의 값이 서로소 관계가 아니라면 최대공약수로 나누면 됨

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
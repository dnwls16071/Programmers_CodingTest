from collections import deque

def solution(cacheSize, cities):
    # dq = deque(iterable, maxlen)  → 최대길이 설정 가능
    # 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용 → 가장 최근에 사용된 페이지를 교체
    # cache hit일 경우 : 1     → CPU가 참조하고자 하는 메모리가 캐시에 존재하고 있을 경우 Cache Hit라고 한다.
    # cache miss일 경우 : 5    → CPU가 참조하고자 하는 메모리가 캐시에 존재하지 않을 때 Cache Miss라고 한다.
    lst = deque(maxlen=cacheSize)
    answer = 0
    for city in cities:
        city = city.lower() # 대소문자 구분을 하지 않으므로 대문자로 통일하든 소문자로 통일하든 두 작업 중 하나의 작업을 필수로 해야함
        if city not in lst:
            lst.append(city)
            answer += 5
        else:
            lst.remove(city)
            lst.append(city)
            answer += 1
    return answer
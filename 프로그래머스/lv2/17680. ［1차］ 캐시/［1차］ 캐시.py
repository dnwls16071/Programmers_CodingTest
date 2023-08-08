from collections import deque

def solution(cacheSize, cities):
    # dq = deque(iterable, maxlen)  → 최대길이 설정 가능
    # 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용 → LRU : 가장 오랫동안 참조되지 않은 페이지를 교체
    # cache hit일 경우 : 1     → CPU가 참조하고자 하는 메모리가 캐시에 존재하고 있을 경우 Cache Hit라고 한다.
    # cache miss일 경우 : 5    → CPU가 참조하고자 하는 메모리가 캐시에 존재하지 않을 때 Cache Miss라고 한다.
    lst = deque(maxlen=cacheSize)       # deque의 최대 길이를 지정
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

# 테스트케이스4 : ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
# ["Jeju"]                                             → 5
# ["Jeju", "Pangyo"]                                   → 10 
# ["Jeju", "Pangyo", "Seoul"]                          → 15
# ["Jeju", "Pangyo", "Seoul", "NewYork"]               → 20
# ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]         → 25
# ["Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco"] → 30
# ["Pangyo", "NewYork", "LA", "SanFrancisco", "Seoul"] → 31
# ["NewYork", "LA", "SanFrancisco", "Seoul", "Rome"]   → 36
# ["LA", "SanFrancisco", "Seoul", "Rome", "Paris"]     → 41
# ["SanFrancisco", "Seoul", "Rome", "Paris", "Jeju"]   → 46
# ["Seoul", "Rome", "Paris", "Jeju", "NewYork"]        → 51
# ["Seoul", "Paris", "Jeju", "NewYork"]                → 52
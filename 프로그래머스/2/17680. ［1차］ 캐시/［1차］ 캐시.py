from collections import deque

def solution(cacheSize, cities):    
    cache = deque(maxlen=cacheSize)
    time = 0
    for city in cities:
        city = city.lower()
        if city not in cache:
            time += 5
        else:
            cache.remove(city)
            time += 1
        cache.append(city)
    return time
            
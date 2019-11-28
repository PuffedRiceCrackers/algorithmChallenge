
from collections import deque

def solution(cacheSize, cities):

    cache = deque([])
    time = 0

    if cacheSize == 0:
        return len(cities) * 5
    else:
        for i in range(len(cities)):
            if cities[i].lower() in cache:
                cache.remove(cities[i].lower())
                cache.append(cities[i].lower())
                time += 1
            else:
                if len(cache) == cacheSize:
                    cache.popleft()
                cache.append(cities[i].lower())
                time += 5
    return time

cacheSize = 3
#cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
solution(cacheSize, cities)
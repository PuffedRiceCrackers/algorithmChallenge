from heapq import heapify, heappop, heappush
def solution(scoville, K):
    heapify(scoville)
    count = 0
    while min(scoville) < K and len(scoville) >= 2:
        min1 = heappop(scoville)
        min2 = heappop(scoville)
        new = min1 + min2 * 2
        heappush(scoville, new)
        count += 1
    
    if min(scoville) >= K:
        return count
    else:
        return -1

scoville = [8]
K = 7

print(solution(scoville, K))
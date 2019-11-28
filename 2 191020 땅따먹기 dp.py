

from random import randint

def solution(land):
    cache = [[-1 for j in range(4)] for i in range(len(land))]
    cache[len(land) - 1] = [land[len(land) - 1][j] for j in range(4)]
    for i in range(2, len(land) + 1):
        for j in range(4):
            cache[len(land) - i][j] = max([cache[len(land) - i + 1][k] for k in range(4) if k != j]) + land[len(land) - i][j]
    return max(cache[0])
            

land = [[1, 2, 3, 5], [5, 6, 7, 100], [4, 3, 2, 1]]
#land = [[randint(1, 5) for i in range(4)] for i in range(5)]
print(land)
solution(land)
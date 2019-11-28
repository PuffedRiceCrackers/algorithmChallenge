

def dp(row, col, cache):
    if row >= len(cache) or col >= len(cache[0]):
        return 0
    elif row == len(cache) - 1 and col == len(cache[0]) - 1:
        return 1
    answer = cache[row][col]
    if answer == -1:
        answer = dp(row + 1, col, cache) + dp(row, col + 1, cache)
        cache[row][col] = answer
    return answer

def solution(m,n):
    cache = [[-1 for j in range(n)] for i in range(m)]
    return dp(0, 0, cache) if m != 0 and n != 0 else 0
    

print(solution(3,3))
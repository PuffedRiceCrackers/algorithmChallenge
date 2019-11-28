def sol(row, col, puddles, cache):
    targetRow = len(cache) - 1
    targetCol = len(cache[0]) - 1
    answer = cache[row][col]
    if answer == -1:
        if row + 1 > targetRow:
            cache[row][col] = sol(row, col + 1, puddles, cache)
        elif col + 1 > targetCol:
            cache[row][col] = sol(row + 1, col, puddles, cache)
        else:
            cache[row][col] = sol(row, col + 1, puddles, cache) + sol(row + 1, col, puddles, cache)
        answer = cache[row][col]
    return answer

def solution(m, n, puddles):
    cache = [[-1 for i in range(n)] for j in range(m)]

    # base case (1) 목적지 바로 앞인 경우
    cache[m - 2][n - 1] = 1
    cache[m - 1][n - 2] = 1

    # base case (2) puddle 인 경우
    for puddle in puddles:
        if puddle:
            cache[puddle[0] - 1][puddle[1] - 1] = 0
    return sol(0, 0, puddles, cache) % 1000000007

m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))
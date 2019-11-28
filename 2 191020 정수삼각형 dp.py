



# recursion
def solution(triangle):
    cache = [[-1 for j in range(len(triangle[i]))] for i in range(len(triangle))]
    def func(a, b):
        nonlocal cache
        if a == len(triangle) - 1:
            return triangle[a][b]
        answer = cache[a][b]
        if answer == -1:
            answer = max(func(a + 1, b), func(a + 1, b + 1)) + triangle[a][b]
            cache[a][b] = answer
        return answer
    return func(0, 0)

# iteration
def solution(triangle):
    cache = [[-1 for j in range(len(triangle[i]))] for i in range(len(triangle))]
    cache[len(triangle) - 1] = [num for num in triangle[len(triangle) - 1]]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[len(triangle) - i - 1])):
            cache[len(triangle) - i - 1][j] = max(cache[len(triangle) - i][j], cache[len(triangle) - i][j + 1]) + triangle[len(triangle) - i - 1][j]
    return cache[0][0]


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(solution(triangle))
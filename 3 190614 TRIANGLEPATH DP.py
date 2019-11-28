def maxSumFrom(row, col):
    global rows
    global triangle
    global cache

    # if last line
    if row == rows - 1:
        return triangle[row][col]

    answer = cache[row][col]

    if answer != -1:
        return answer
    
    answer = triangle[row][col] + max(maxSumFrom(row + 1, col),maxSumFrom(row + 1, col + 1))
    cache[row][col] = answer
    return answer

tests = int(input())
for test in range(tests):     
    rows = int(input())
    triangle = []
    cache = []
    for row in range(rows):
        triangle.append(list(map(int, input().split())))
        cache.append([-1 for i in range(row + 1)])
    print(maxSumFrom(0, 0))
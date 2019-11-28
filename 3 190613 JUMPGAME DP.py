
def waysToTopLeftFrom(row, col):
    global matrix
    global cache
    
    if row == 0 and col == 0:
        return 'YES'
    
    answer = cache[row][col]

# case 1) already calculated : return
    if answer != -1:
        return answer
    
# case 2) not calculated yet
    # left side
    for i in range(col):
        if matrix[row][i] == col - i:
            if waysToTopLeftFrom(row, i) == 'YES':
                answer = 'YES'

    # upper side
    for i in range(row):
        if matrix[i][col] == row - i:
            if waysToTopLeftFrom(i, col) == 'YES':
                answer = 'YES'

    if answer == -1:
        answer = 'NO'
    cache[row][col] = answer
    return answer

tests = int(input())
for test in range(tests):
    matrixSize = int(input())
    matrix = [list(map(int, input().split())) for row in range(matrixSize)]
    cache = [[-1 for i in range(matrixSize)] for i in range(matrixSize)]
    print(waysToTopLeftFrom(matrixSize - 1, matrixSize - 1))

# a = '''2 5 1 6 1 4 1
# 6 1 1 2 2 9 3
# 7 2 3 2 1 3 1
# 1 1 3 1 7 1 2
# 4 1 2 3 4 1 2
# 3 3 1 2 3 4 1
# 1 5 2 9 4 7 0 '''
# b = '''2 5 1 6 1 4 1
# 6 1 1 2 2 9 3
# 7 2 3 2 1 3 1
# 1 1 3 1 7 1 2
# 4 1 2 3 4 1 3
# 3 3 1 2 3 4 1
# 1 5 2 9 4 7 0 '''
# matrix = [list(map(int, (a.splitlines())[i].split())) for i in range(7)]
# matrix = [list(map(int, (b.splitlines())[i].split())) for i in range(7)]
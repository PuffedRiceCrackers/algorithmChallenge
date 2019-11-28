def maxSumFrom(row, col):
    global size
    global triangle
    global sumCache 
    if row == size - 1:
        return triangle[row][col]

    answer = sumCache[row][col]
    
    if answer == -1:
        answer = triangle[row][col] + max(maxSumFrom(row + 1, col), maxSumFrom(row + 1, col + 1))
        sumCache[row][col] = answer
    return answer

def numOfMaxPathFrom(row, col):
    global size
    global triangle
    global pathCache 

    if row == size - 1:
        return 1

    answer = pathCache[row][col]

    if answer == -1:
        maxSumUnder = maxSumFrom(row + 1, col)
        maxSumDiagonal = maxSumFrom(row + 1, col + 1)

        # if max sum of 2 sub triangles are the same -> both paths are added
        if maxSumUnder == maxSumDiagonal:
            answer = numOfMaxPathFrom(row + 1, col) + numOfMaxPathFrom(row + 1, col + 1)
        else:
            # else, paths of triangles with the max sums are reflected
            biggerSum = maxSumUnder > maxSumDiagonal and 'under' or 'diagonal'
            if biggerSum == 'under':
                answer = numOfMaxPathFrom(row + 1, col)
            elif biggerSum == 'diagonal':
                answer = numOfMaxPathFrom(row + 1, col + 1)
        pathCache[row][col] = answer
    return answer

tests = int(input())
for test in range(tests):
    size = int(input())
    triangle = []
    for row in range(size):
        triangle.append(list(map(int, input().split())))
    sumCache = [[ -1 for col in range(height + 1)] for height in range(size)]
    pathCache = [[-1 for col in range(height + 1)] for height in range(size)]
    print(numOfMaxPathFrom(0,0))
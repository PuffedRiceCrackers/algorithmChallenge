

def solution(arr1, arr2):
    rows = len(arr1)
    joined = len(arr2)
    cols = len(arr2[0])
    answer = [["None" for col in range(cols)] for row in range(rows)]
    for row in range(rows):
        for col in range(cols):
            temp = 0
            for a, b in zip([arr1[row][i] for i in range(joined)], [arr2[j][col] for j in range(joined)]):
                temp += a * b
            answer[row][col] = temp
    return answer      

# arr1=[[1, 4], [3, 2], [4, 1]]
# arr2=[[3, 3], [3, 3]]

arr1=[[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2=[[5, 4], [2, 4], [3, 1]]

solution(arr1, arr2)

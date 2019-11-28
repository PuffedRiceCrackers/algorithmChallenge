from functools import reduce

def partition(A, start, end):
        wall = start - 1
        pivot = A[end]
        for i in range(start, end):         
            if (int(A[i] + pivot) > int(pivot + A[i]) and A[i] or pivot) == A[i]:
                wall += 1
                A[wall], A[i] = A[i], A[wall]
        A[wall + 1], A[end] = A[end], A[wall + 1]
        return wall + 1
    
def quickSort(A, start, end):
    if start < end:
        wall = partition(A, start, end)
        quickSort(A, start, wall - 1)
        quickSort(A, wall + 1, end)
    return A

def solution(numbers):
    numbers = [str(num) for num in numbers]
    numbers = quickSort(numbers, 0, len(numbers)-1)
    return str(int(reduce(lambda x, y: x + y, numbers, '')))
    
numbers = [0, 0, 0, 0, 0]
print(solution(numbers))

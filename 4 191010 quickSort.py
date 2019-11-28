def partition(A, start, end):
        wall = start - 1
        pivot = A[end]

        for i in range(start, end):
            if A[i] <= pivot:
                wall += 1
                A[wall], A[i] = A[i], A[wall]
        A[wall + 1], A[end] = A[end], A[wall + 1]
        return wall + 1
    
def quickSort(A, start, end):
    if start < end:
        wall = partition(A, start, end)
        print(A)
        quickSort(A, start, wall - 1)
        quickSort(A, wall + 1, end)
    return A

print(quickSort([72, 30, 5, 9, 34], 0, 4))


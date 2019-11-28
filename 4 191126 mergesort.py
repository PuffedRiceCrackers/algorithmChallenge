



def mergeSort(a, start, end):
    if start == end:
        return [a[start]]
    left = mergeSort(a, start, int((start + end) / 2))
    right = mergeSort(a, int((start + end) / 2) + 1, end)
    i, j = 0, 0
    answer = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            answer.append(left[i])
            i += 1
        elif left[i] > right[j]:
            answer.append(right[j])
            j += 1
    if len(left[i:]) != 0:
        answer.extend(left[i:])
    elif len(right[j:]) != 0:
        answer.extend(right[j:])
    return answer

print(mergeSort([3, 2], 0, 1))

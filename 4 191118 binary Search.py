def binarySearchInsert(List, start, end, a):
    if start <= end:
        middle = int((start + end) / 2)
        if a < List[middle]:
            binarySearchInsert(List, start, middle - 1, a)
        elif a > List[middle]:
            binarySearchInsert(List, middle + 1, end, a)
        else:
            List.insert(middle, a)
    else:
        List.insert(start, a)

def binarySearch(List, start, end, a):
    if start <= end:
        middle = int((start + end) / 2)
        if a < List[middle]:
            return binarySearch(List, start, middle - 1, a)
        elif a > List[middle]:
            return binarySearch(List, middle + 1, end, a)
        else:
            return True
    else:
        return False


    
List = [1, 1, 2, 3, 4, 4, 5, 6, 6]
List.sort()
print(binarySearch(List, 0, len(List) - 1, 0))

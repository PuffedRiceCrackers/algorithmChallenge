# extend only to bigger end
def maxWidthIncluding(plates, first, last):
    mid = int((first + last) / 2)
    maxWidth = plates[mid]
    start, end = mid, mid
    width = 1
    while 1:
        width += 1

        # (1) start/end all reached the edge 
        if start == first and end == last:
            break
    
        # (2) Only one in start or end reached the edge -> move the one that didn't reached the end
        if start == first:
            end += 1
        elif end == last:
            start -= 1

        # (3) neither start nor end reached the end -> compare the side rectangles, expand to the bigger one
        else:
            if plates[start-1] >= plates[end+1]:
                start -= 1
            elif plates[start-1] < plates[end+1]:     
                end += 1

        maxWidth = max(maxWidth, min(plates[start:end + 1]) * width)
    return maxWidth

def maxWidthOf(plates, first, last):
    if last - first == 0:                  # 1 plate
        return plates[first]
    elif last - first == 1:                # 2 plates
        return max(min(plates[first], plates[last]) * 2, plates[first], plates[last])
    else:                                  # 3 or more plates
        mid = int((first + last) / 2)
        return max(maxWidthOf(plates, first, mid-1), maxWidthIncluding(plates,first,last), maxWidthOf(plates, mid+1, last))

tests = int(input())
for test in range(tests):
    numPlate = int(input())
    plates = list(map(int, input().split()))
    print(maxWidthOf(plates, 0, numPlate - 1))

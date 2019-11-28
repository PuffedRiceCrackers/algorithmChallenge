
# mid 포함한 모든 사각형 combination 을 비교
def maxWidthIncluding(plates, first, last):
    mid = int((first + last) / 2)
    tempMax = -1
    for length in range(last - first):
        if mid - length >= first:
            start = mid-length
        elif mid - length < first:
            start = first
        end = start + length
        while start <= mid and end <= last:
            tempMax = max(tempMax, min(plates[start:end + 1]) * (length+1))
            start += 1
            end += 1
    return tempMax

def maxWidthOf(plates, first, last):
    if last - first == 0:                  # 판자가 1개
        return plates[first]
    elif last - first == 1:                # 판자가 2개
        return max(min(plates[first], plates[last]) * 2, plates[first], plates[last])
    else:                                  # 판자가 3개~
        mid = int((first + last) / 2)
        # mid를 기준으로 mid왼쪽에 답이 있는 경우, mid를 포함하여 답이 있는 경우, mid의 오른쪽에 답이 있는 경우
        return max(maxWidthOf(plates, first, mid-1), maxWidthIncluding(plates,first,last), maxWidthOf(plates, mid+1, last))

tests = int(input())
for test in range(tests):
    numPlate = int(input())
    plates = list(map(int, input().split()))
    print(maxWidthOf(plates, 0, numPlate - 1))

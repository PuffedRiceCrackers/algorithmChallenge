def maxBoardOf(plates, endPlate):
    if endPlate == 0:
        return plates[0]
    elif endPlate != 0:
        maxWidth = -1 # max width including end plate
        for count in range(endPlate+1):
            maxWidth = max(maxWidth, min(plates[endPlate - count:endPlate+1])*(count+1))
        return max(maxWidth, maxBoardOf(plates, endPlate-1))

tests = int(input())
answers = []
for test in range(tests):
    numPlate = int(input())
    plates = list(map(int, input().split()))
    answers.append(maxBoardOf(plates, numPlate - 1))

for answer in answers:
    print(answer)

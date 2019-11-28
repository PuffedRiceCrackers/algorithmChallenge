def divide(pic):
    subSquare = []
    for count in range(4):
        if len(pic)!=0:
            if pic[0] != 'x':
                subSquare.append(pic[0])
                del pic[0]
            elif pic[0] == 'x':
                del pic[0]
                subSquare.append(divide(pic))
    if len(subSquare) == 4:
        subSquare[0], subSquare[1], subSquare[2], subSquare[3] = subSquare[2], subSquare[3], subSquare[0], subSquare[1]
        subSquare.insert(0,'x')
        subSquare = ''.join(subSquare)
    return subSquare

testNum = int(input())
answers = []
for test in range(testNum):
    pic = list(input())
    answers.append(divide(pic))

for answer in answers:
    print(answer[0])
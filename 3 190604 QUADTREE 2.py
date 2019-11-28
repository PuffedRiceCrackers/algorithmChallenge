def divide(pic, start):
    if pic[start] != 'x':
            return pic[start]
    elif pic[start] == 'xㄴ':
        start += 1
        temp = []
        for quadrant in range(4):
            quad = divide(pic, start)
            temp.append(quad)
            start += len(quad)
    return 'x'+temp[2]+temp[3]+temp[0]+temp[1]

testNum = int(input())
answers = []
for test in range(testNum):
    pic = input()
    answers.append(divide(pic,0))

for answer in answers:
    print(answer)
    

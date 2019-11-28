import copy

def checkRdD(board, point, output):
    if board[point['row']][point['col'] + 1] == '.' and board[point['row'] + 1][point['col']] == '.':
        output['RdD'] = 1
        output['total'] += 1

def checkRD(board, point, output):
    if board[point['row']][point['col'] + 1] == '.' and board[point['row'] + 1][point['col']+1] == '.':
        output['RD'] = 1
        output['total'] += 1

def checkDL(board, point, output):
    if board[point['row'] + 1][point['col']] == '.' and board[point['row'] + 1][point['col'] - 1] == '.':
        output['DL'] = 1
        output['total'] += 1
    
def checkDR(board, point, output):
    if board[point['row'] + 1][point['col']] == '.' and board[point['row'] + 1][point['col'] + 1] == '.':
        output['DR'] = 1
        output['total'] += 1
    
def canPutLShape(board, point):
    global height
    global width
    output = {'RdD': 0, 'DL': 0, 'RD': 0, 'DR': 0, 'total':0}

    # case 1) 마지막 줄이면 할 수 있는게 없음 (순서강제)
    if point['row'] == height - 1:
        return output

    # case 2) 마지막 줄이 아니라면 col 위치에 따라 가능한 L이 달라짐
    else:
        # subcase 1) 첫 col에 위치
        if point['col'] == 0:
            checkRdD(board, point, output)
            checkRD(board, point, output)
            checkDR(board, point, output)
        # subcase 2) 마지막 col에 위치
        elif point['col'] == width - 1:
            checkDL(board, point, output)
        # subcase 3) 중간에 위치
        else:
            checkRdD(board, point, output)
            checkRD(board, point, output)
            checkDL(board, point, output)
            checkDR(board, point, output)
    return output    

def movePointToWhitePoint(board, point):
    global answer
    # white가 나올 때까지 점을 left->right, top->bottom순서로 옮겨준다
    while 1:
        # case 1) point 가 흰색 - return
        if board[point['row']][point['col']] == '.':
            break
        # case 2) point 가 흰색이 아님 (움직여 주던가, 움직일 수 없으면 return)
        else:
            if point['col'] == width - 1:
                # subcase 1) point 가 board 의 끝점인데 흰색도 아님 - 여기까지 왔으면 위에서 다 black으로 색칠 한 것
                if point['row'] == height - 1:
                    answer += 1
                    return 
                # subcase 2) point 가 board 의 마지막 col - 줄바꿈
                else:
                    point['col'] = 0
                    point['row'] += 1
            # subcase 3) point 가 마지막 col 도 아니고, 마지막 row 도 아닌 경우 - 한칸 옆으로
            else:
                point['col'] += 1
    return

def paintPointsBlack(board, point0, point1, point2):
    board[point0['row']][point0['col']] = '#'
    board[point1['row']][point1['col']] = '#'
    board[point2['row']][point2['col']] = '#'
    return board

# #검은칸, .흰색칸
def fillBoardWithL(board, point):
    global height
    global width

    # point 를 white가 있는 곳까지 옮긴다
    movePointToWhitePoint(board, point)

    # case 1 : 찾은 흰색이 마지막 row 에 있음 - 어떻게 해도 안될거니 그냥 return
    if point['row'] == height - 1:
        return
    # case 2 : 흰색이 마지막 row 에 있지 않음 - L이 들어가는지 확인
    elif point['row'] != height - 1:
        # record how L can fit around current point
        LCanFit = canPutLShape(board, point)        
        if LCanFit['total'] != 0:
            # if certain shape is viable, call itself again with blackened board
            if LCanFit['RdD'] == 1:
                point1 = {'row': point['row'], 'col': point['col'] + 1}
                point2 = {'row': point['row']+1, 'col': point['col']}
                fillBoardWithL(paintPointsBlack(copy.deepcopy(board), point, point1, point2), copy.deepcopy(point))

            if LCanFit['DL'] == 1:
                point1 = {'row': point['row'] + 1, 'col': point['col']}
                point2 = {'row': point['row'] + 1, 'col': point['col'] - 1}
                fillBoardWithL(paintPointsBlack(copy.deepcopy(board), point, point1, point2), copy.deepcopy(point))

            if LCanFit['RD'] == 1:
                point1 = {'row': point['row'], 'col': point['col']+1}
                point2 = {'row': point['row']+1, 'col': point['col']+1}
                fillBoardWithL(paintPointsBlack(copy.deepcopy(board), point, point1, point2), copy.deepcopy(point))

            if LCanFit['DR'] == 1:
                point1 = {'row': point['row']+1, 'col': point['col']}
                point2 = {'row': point['row']+1, 'col': point['col']+1}
                fillBoardWithL(paintPointsBlack(copy.deepcopy(board), point, point1, point2), copy.deepcopy(point))
        else:
            return


numTest = int(input())
answers = []
for test in range(numTest):
    board = []            
    answer = 0

    # Turn input into 'board'
    height, width = map(int, input().split())
    for row in range(height):
        board.append(list(input()))

    # start operation
    if height == 1 or width == 1:
        print(0)
    else:
        point = {'row':0, 'col':0}
        fillBoardWithL(board, point)
        answers.append(answer)

for answer in answers:
    print(answer)




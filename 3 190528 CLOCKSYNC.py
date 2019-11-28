import copy

def areAllClocks12(buttonPushTable):
    global clockStatus
    global clocksLinkedToButton

    changedClockStatus = copy.deepcopy(clockStatus)
    for buttonIdx in range(len(buttonPushTable)):                   
        numToPush = buttonPushTable[buttonIdx]                   # How many times to push
        if numToPush != 0:
            for clock in clocksLinkedToButton[buttonIdx]:        # Rotate all clocks linked to the button
                changedClockStatus[clock] += (numToPush * 3)
                changedClockStatus[clock] %= 12

    # Check if all clocks are on 12(0)
    for clock in changedClockStatus:
        if clock != 0:
            return False
    return True

def recursion(targetButton, buttonPushTable):
    if targetButton == 10:
        if areAllClocks12(buttonPushTable):
            temp = 0
            for pushCount in buttonPushTable:
                temp += pushCount
            global minPush
            minPush = min(minPush, temp)
    else:
        for option in [0, 1, 2, 3]:
            copiedButtonPushTable = copy.deepcopy(buttonPushTable)
            copiedButtonPushTable.append(option)
            recursion(targetButton + 1, copiedButtonPushTable)
        
# clocks linked to a button
clocksLinkedToButton = [
    [0, 1, 2],               # button 0
    [3, 7, 9, 11],           
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]         # button 9
    ]


numTestCase = int(input())

for test in range(numTestCase):

    # get input
    clockStatus = list(map(int, input().split()))
    for clockIdx in range(len(clockStatus)):
        if clockStatus[clockIdx] == 12:
            clockStatus[clockIdx] = 0

    # global var
    targetButton = 0
    minPush = 1000

    # operation
    recursion(targetButton, [])

    # output
    if minPush == 1000:
        print(-1)
    else:
        print(minPush)


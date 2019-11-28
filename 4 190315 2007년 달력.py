# -*- coding: utf-8 -*-

# 기본정보 - [0][0], [0][1]은 편의상 비워둠
MonthDayList = [[0,0],[1,31],[2,28],[3,31],[4,30],[5,31],
                [6,30],[7,31],[8,31],[9,30],[10,31],[11,30],[12,31]]

# 날짜%7 했을때 [일, 월,화,수,목,금,토,일] 인 날짜가 공통적으로 갖게되는 나머지 --> 요일 identifier
dayIdentifier = [0,1,2,3,4,5,6]

# 입력부분
stringInput = input()
targetMonth, targetDay = stringInput.split()
targetMonth = int(targetMonth)
targetDay = int(targetDay)

# 달이 넘어갈 때마다, dayIdentifier가 바뀌어야 함
def updateIdentifier(tempMonth):
    idxOfLastDay = dayIdentifier.index(MonthDayList[tempMonth][1]%7)
    for i in range(7):
        dayIdentifier[(idxOfLastDay+i)%7]=i
        
# X월이면 X-1번만 dayIdentifier를 바꿔준다
for tempMonth in range(targetMonth-1):
    updateIdentifier(tempMonth+1)
    
if dayIdentifier.index(targetDay%7) == 0:
    print("SUN")
elif dayIdentifier.index(targetDay%7) == 1:
    print("MON")
elif dayIdentifier.index(targetDay%7) == 2:
    print("TUE")
elif dayIdentifier.index(targetDay%7) == 3:
    print("WED")
elif dayIdentifier.index(targetDay%7) == 4:
    print("THU")
elif dayIdentifier.index(targetDay%7) == 5:
    print("FRI")
else:
    print("SAT")
    

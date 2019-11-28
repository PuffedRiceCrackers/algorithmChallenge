
# make 2d Array from input
def into2dArray(pairData):
    finalArray = []
    subArray = []
    isSubArrayFull = False
    for student in pairData:
        subArray.append(student)
        isSubArrayFull = (len(subArray)==2)
        if isSubArrayFull == True:
            finalArray.append(subArray)
            subArray = []
    return finalArray

# return friend of 'Robert' among list 'students'
def friendsOf(Robert, students):
    global pairData
    friendsOfRobert = []
    for pair in pairData:
        if pair[0] == Robert:
            if pair[1] in students:
                friendsOfRobert.append(pair[1])
        elif pair[1] == Robert:
            if pair[0] in students:
                friendsOfRobert.append(pair[0])
    return friendsOfRobert

# remove a new pair from students
def removePairFromStudents(students, friend, Robert):
    unpairedStudents = students[:]
    for student in students:
        if student == friend:
            unpairedStudents.remove(friend)
        if student == Robert:
            unpairedStudents.remove(Robert)
    return unpairedStudents

# Find pair of 'Robert'
# Recursively make subproblem where 'Robert' and his friend are removed from the set
def findPair(students, Robert):
    global answer

    if len(students) == 0:
        return
    friendsOfRobert = friendsOf(Robert, students)

    # case 1 : Robert has 0 friend
    if len(friendsOfRobert) == 0:
        return
    # case 2 : Robert has friends
    else:
        # Only 2 students left : pair them, and return
        if len(students) == 2:
            answer += 1  
            return
        # More than 2 students left  : recursively call function
        else:
            for friend in friendsOfRobert:
                # remove already paired one (Robert, friend) + recursively call subproblem
                leftStudents = removePairFromStudents(students[:], friend, Robert)
                if len(leftStudents) != 0:
                    findPair(leftStudents, leftStudents[0])
            return

numTestCase = int(input())
finalOutput = []
for test in range(numTestCase):

    # make pairData
    numStudent, numPairOfFriend = map(int, input().split())

    pairData = into2dArray(list(map(int, input().split())))
    studentList = list(range(numStudent))

    # init global variable
    answer = 0

    # findPair of 'studentList[0]', in studentList
    # 3rd arg : 
    findPair(studentList, studentList[0])
    finalOutput.append(answer)

# output
for answer in finalOutput:
    print(answer)



# 시간초과
import copy

# Re-order heating array to correspond to sorted eating array 
def reorder():
    global originalHeating
    global originalEating
    global eating
    reOrderedHeating = []
    for i in range(len(eating)):
        value = eating[i]                   
        idx = originalEating.index(value)               
        reOrderedHeating.append(originalHeating[idx])
        originalEating[idx] = -1 # avoid duplicate
    return reOrderedHeating

def sequence():
    global heating
    global eating
    answer = 0
    cookingTime = 0
    for i in range(len(eating)):
        cookingTime += heating[i]
        answer = max(answer, cookingTime + eating[i])
    return answer
    
tests = int(input())
for test in range(tests):
    numberOfLunchBoxes = int(input())
    originalHeating = list(map(int, input().split()))
    originalEating = list(map(int, input().split()))

    eating = copy.deepcopy(originalEating)
    eating.sort(reverse=True)
    heating = reorder()

    print(sequence())
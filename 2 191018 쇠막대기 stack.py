def solution(arrangement):
    arrangement = arrangement.replace('()', 'R')
    stack = []
    pieces = 0
    for i in range(len(arrangement)):
        if arrangement[i] == "R":
            pieces += len(stack)
        elif arrangement[i] == "(":
            stack.append(1)
        elif arrangement[i] == ")":
            stack.pop()
            pieces += 1
    return pieces


arrangement = "()(((()())(())()))(())"
print(solution(arrangement))

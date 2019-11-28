def solution(raw):
    global opener
    global closer
    stack = []

    for bracket in raw:
        if bracket in opener:
            stack.append(bracket)
        elif bracket in closer:
            
            try:# 처음부터 closer를 줄 수 있으므로
                
                # 교차
                if opener[closer.index(bracket)] != stack[-1]:
                    return 'NO'
                # 교차하진 않는 경우 - 끝까지
                else:
                    stack.pop()
            except:
                return 'NO'

    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'

opener = ["{", "[", "("]
closer = ["}", "]", ")"]

numTestCase = int(input())
for test in range(numTestCase):
    raw = list(input())
    print(solution(raw))

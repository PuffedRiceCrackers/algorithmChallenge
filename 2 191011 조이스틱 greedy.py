def solution(name):
    order = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    name = list(name)
    
    # 이동 횟수 계산
    noneA = [i for i in range(len(name)) if name[i] != "A"]
    count = 0
    currPos = 0
    while noneA:
        nextPos = min(noneA, key=lambda x: abs(currPos - x) > int(len(name) / 2) and len(name) - abs(currPos - x) or abs(currPos - x))
        count += abs(currPos - nextPos) > int(len(name) / 2) and len(name) - abs(currPos - nextPos) or abs(currPos - nextPos)
        noneA.remove(nextPos)
        currPos = nextPos
    
    # 조이스틱 조작횟수 계산
    joyStick = [order.index(alphabet) if alphabet in order[0:13] else 26 - order.index(alphabet) for alphabet in name]
    return sum(joyStick) + count

name = "JAZ"
name = "XXAAAAAAAAXX"
name = "C"

print(solution(name))
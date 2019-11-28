# 0903_pg_프린터.py

from collections import deque

def solution(priorities, location):
    printCount = 0
    que = deque(priorities)

    while len(que) != 0:

        doc = que.popleft()

        if que:
            # 타겟 doc
            if location == 0:
                if que and doc >= max(que):       #인쇄
                    printCount += 1
                    return printCount
                else:                      #뒤로보냄
                    que.append(doc) 
                    location = len(que) - 1
            # 타겟 doc이 아님
            else:
                if que and doc >= max(que):         #인쇄
                    printCount += 1
                else:                       #뒤로보냄
                    que.append(doc)
                location -= 1
        else:
            return len(priorities)

priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))
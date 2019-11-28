
from collections import deque
from copy import deepcopy

def solution(heights):
    answer = [-1 for item in heights]
    notFound = deque()

    while heights:
        idx = len(heights)
        pole = heights.pop()
        print(f"idx = {idx}, pole = {pole}")
        # not found 들을 기록함

        for item in deepcopy(notFound):
            print(f"item = {item}")
            if item[1] < pole:
                answer[item[0] - 1] = idx
                notFound.remove((item[0], item[1]))
            print(f"answer = {answer}")
        
        # notFound 에 넣는다
        notFound.append((idx, pole))
        print(f"notFound = {notFound}")
        print("")
    
    answer = [item if item != -1 else 0 for item in answer]
    print(answer)


heights = [3,9,9,3,5,7,2]
solution(heights)


# 프린트 지운 버전 
# from collections import deque
# from copy import deepcopy

# def solution(heights):
#     answer = [-1 for item in heights]
#     notFound = deque()
#     while heights:
#         idx = len(heights)
#         pole = heights.pop()
#         for item in deepcopy(notFound):
#             if item[1] < pole:
#                 answer[item[0] - 1] = idx
#                 notFound.remove((item[0], item[1]))
#         notFound.append((idx, pole))
#     answer = [item if item != -1 else 0 for item in answer]
#     return answer

# heights = [3, 9, 9, 3, 5, 7, 2]
# print(solution(heights))

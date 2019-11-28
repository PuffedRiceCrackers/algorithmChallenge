# Counter를 사용한 버전
from collections import Counter
from functools import reduce
def solution3(clothes):
    c = Counter()
    for item in clothes:
        c[item[1]] += 1
    return reduce(lambda x, y: x * (y + 1), c.values(), 1) - 1

def solution2(clothes):
    # dict 를 만듦
    clothesDict = {}
    for item in clothes:
        if item[-1] not in clothesDict.keys():
            clothesDict[item[-1]] = 1
        else:
            clothesDict[item[-1]] += 1
    # 조합 계산
    answer = 1
    for itemCount in clothesDict.values():
        answer *= (itemCount + 1)
    return answer - 1

# 조합을 사용한 버전 - 시간초과
from itertools import combinations
def solution1(clothes):
    # dict 를 만듦
    clothesDict = {}
    for item in clothes:
        if item[-1] not in clothesDict.keys():
            clothesDict[item[-1]] = [item[0]]
        else:
            clothesDict[item[-1]].append(item[0])
    # 조합 계산
    answer = 0
    for numOfTypes in range(1, len(clothesDict) + 1):  # 3개 타입을 입을 것이다
        for typeComb in combinations(clothesDict.keys(), numOfTypes):  # 여러 타입중 어떤 3개 타입을 선택할 것인지
            temp = 1
            for item in typeComb:
                temp *= len(clothesDict[item])
            answer += temp
    return answer

clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
#clothes = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]

print(solution1(clothes))
print(solution2(clothes))
print(solution3(clothes))

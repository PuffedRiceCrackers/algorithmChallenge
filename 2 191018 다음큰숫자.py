from collections import Counter
def solution(n):

    original = list("{0:b}".format(n))
    smallestOne = None

    # 가장 끝에 있는 1을 찾는다
    for i in range(len(original)):
        if original[len(original) - i - 1] == '1':
            smallestOne = i
            break

    # 1이 있는 가장 끝 자리에서 증가시키면, 1의 개수를 늘리지 않으면서 가장 최소폭으로 증가할 수 있음
    temp = n + 2 ** (smallestOne)
    temp = list("{0:b}".format(temp))

    # 1→0 으로 바뀐 애들의 개수를 구한다
    oneToAdd = Counter(original)['1'] - Counter(temp)['1']
    count = 0
    for i in range(len(temp)):
        if temp[len(temp) - i - 1] == '0' and count < oneToAdd:
            temp[len(temp) - i - 1] = '1'
            count += 1
        if count == oneToAdd:
            break

    # 1→0 으로 바뀐 애들을 뒤에서부터 채운다
    temp = list(map(lambda x: int(x), temp))
    answer = 0
    for i in range(len(temp)):
        answer += 2 ** (len(temp) - i - 1) * temp[i]
        
    return answer
    
    
n = 24
solution(n)
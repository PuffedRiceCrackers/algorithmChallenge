# 세 숫자에는 중복이 없다는 것과
# 숫자 0은 포함되지 않는다는 점

from itertools import combinations
def solution(baseball):
    # [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]	

    for hint in baseball:
        numbers = list(str(hint[0]))
        strike = hint[1]
        ball = hint[2]
        out = 3 - strike - ball

        cases = list(permutations('s'*strike + 'b'*ball + 'o'*out, 3)))
        for case in cases:
            
            temp = []
            for i in range(len(case)):
                if case[i] == 's':
                    temp.append(set(numbers[i]))
                elif case[i] == 'o':
                    temp.append(set(map(lambda a: str(a), {1, 2, 3, 4, 5, 6, 7, 8, 9})) - {numbers})
                else:
                    tmep.append(-1)

            for i in range(len(temp)):
                if temp[i] == 


        









    
#candidates = [(a*100 + b * 10 + c, True) for a in range(1, 10) for b in range(1, 10) for c in range(1, 10)]

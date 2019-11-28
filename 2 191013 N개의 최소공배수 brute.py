from functools import reduce
def solution(arr):
    answer = dict()
    for num in arr:
        i = 1
        while num != 1:
            i += 1
            count = 0
            while num % i == 0:
                count += 1
                num = num // i
            if count != 0:
                if not answer.get(i):
                    answer[i] = count
                else:
                    answer[i] = count if count > answer[i] else answer[i]
    return reduce(lambda x,y:x*y, [ k**v for k,v in answer.items()], 1)
            
arr = [2, 6, 8, 14]
arr = [2, 3, 4, 5]
arr = [1, 12, 90]
print(solution(arr))
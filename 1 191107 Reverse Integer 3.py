
from math import log10
def reverse(num):
    isPos = num > 0 and True or False
    num = abs(num)
    if num == 0:
        return 0
    else:
        cipher = log10(num)
        answer = 0 
        for i in reversed(range(int(cipher) + 1)):
            answer += (num % 10) * (10 ** i)
            num = num // 10
        answer = isPos and answer or - answer
        return answer if - (2 ** 31) <= answer <= (2 ** 31) - 1 else 0
print(reverse(101))
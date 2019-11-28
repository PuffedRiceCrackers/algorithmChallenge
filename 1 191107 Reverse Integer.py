from math import log10
def reverse(num):
    if num == 0:
        return 0
    else:
        isPos = abs(num) == num and True or False
        num = abs(num)
        cipher = int(log10(num))
        answer = 0
        for i in reversed(range(cipher + 1)):
            temp = num / (10 ** i)
            answer += int(temp) * (10 ** (cipher - i))
            num -= int(temp) * (10 ** i)
        answer = isPos and answer or - answer
        return 0 if answer >= 2 ** 31 or answer <= -2 ** 31 - 1 else answer
print(reverse(101))
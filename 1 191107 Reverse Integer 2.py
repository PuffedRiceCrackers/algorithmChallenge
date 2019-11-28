
from math import log10
def reverse(num):
    isPos = num > 0 and True or False
    num = str(abs(num))
    if num == '0':
        return 0
    else:
        num = int(''.join(list(reversed(num))))
    num = isPos and num or -num
    return num if -2**31 <= num <= 2**31-1 else 0

print(reverse(101))
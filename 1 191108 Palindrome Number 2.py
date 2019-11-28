
from math import log10
def isPalindrome(num):
    if num < 0:
        return False
    elif num == 0:
        return True
    else:
        originalNum = num
        cipher = int(log10(num))
        reverse = 0
        for i in reversed(range(cipher + 1)):
            reverse += (num % 10) * (10 ** i)
            num = num // 10
        return reverse == originalNum
print(isPalindrome(312))


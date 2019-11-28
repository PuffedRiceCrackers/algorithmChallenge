
from math import log10
def isPalindrome(num):
    if num < 0:
        return False
    elif num == 0:
        return True
    else:
        cipher = int(log10(num))
        reverse = 0
        for i in reversed(range(cipher + 1)):
            first = int(num/10**i)
            reverse += first * (10 ** (cipher - i))
            updatedNum = num - first * (10 ** i)
            if num == reverse or updatedNum == reverse:
                return True
            num = updatedNum     
        return False

print(isPalindrome(253))
            
    
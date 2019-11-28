

def isPalindrome(num):
    if num < 0:
        return False
    else:
        return num == int(''.join(list(reversed(str(num)))))
        


    #int(''.join(list(reversed(str(num))))))


print(isPalindrome(10))


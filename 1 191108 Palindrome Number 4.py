
def isPalindrome(num):
    if num == 0:
        return True
    elif num < 0 or num % 10 == 0:
        return False
    else:
        reverse = 0
        while True:
            last = num % 10
            reverse = reverse * 10 + last
            updated = num // 10
            if updated <= reverse:
                return reverse == updated or reverse == num and True or False
            num = updated
        return False

print(isPalindrome(0))
            
    
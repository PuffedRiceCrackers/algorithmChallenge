
def solution(s):
    s = list(s)
    upperFlag = True
    for i in range(len(s)):
        if s[i] == ' ':
            upperFlag = True
        else:
            if upperFlag == True:
                s[i] = s[i].upper()
                upperFlag = False
            elif upperFlag == False:
                s[i] = s[i].lower()
    
    return ''.join(s)
        
s = "for the last week"
solution(s)

# 3people Unfollowed Me
# for the last week
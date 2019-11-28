



def lengthOfLongestSubstring(s):
    maxLen = 1 if s else 0
    for i in range(len(s)):
        used = {s[i]: True}
        for j in range(i + 1, len(s)):
            if used.get(s[j]) == None:
                used[s[j]] = True
            else:
                break
        if len(used.keys()) > maxLen:
            maxLen = len(used.keys())
    return maxLen
    
print(lengthOfLongestSubstring(""))

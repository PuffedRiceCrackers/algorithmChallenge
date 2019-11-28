def longestCommonPrefix(strs):
    try:
        prefix = strs[0]
        for i in range(1, len(strs)):
            newPrefix = ''
            for m, n in zip(prefix, strs[i]):
                if m == n:
                    newPrefix += m
                else:
                    break
            prefix = newPrefix
        return prefix
    except:
        return ''

strs = ["aca", "cba"]
#strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
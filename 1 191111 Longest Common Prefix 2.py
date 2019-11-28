def longestCommonPrefix(strs):
    prefix = ''
    try:
        j = 0
        while True:
            nextAlphabet = strs[0][j]
            for i in range(1, len(strs)):
                if strs[i][j] != nextAlphabet:
                    return prefix
            else:
                prefix += nextAlphabet
                j += 1
    except:
        return prefix

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
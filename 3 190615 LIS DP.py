# max length of subsequence whose min has index of minIdx
def lenOfMaxSeqWith(minIdx):
    global cache
    global sequence
    global length

    # edge case
    if minIdx == length - 1:
        return 1

    answer = cache[minIdx]
    # if not calculated
    if answer == -1:
        answer = 1     # even if there is no subsequence, at least itself should be counted
        for next in range(minIdx + 1, length):
            if sequence[next] > sequence[minIdx]:
                answer = max(answer, lenOfMaxSeqWith(next) + 1)
        cache[minIdx] = answer
    return answer
    
tests = int(input())
for test in range(tests): 
    length = int(input())
    cache = [-1 for i in range(length)]
    sequence = list(map(int, input().split()))
    answer = -1
    for i in range(length):
        answer = max(answer, lenOfMaxSeqWith(i))
    print(answer)

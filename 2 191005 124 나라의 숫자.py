        # global N
        # global i
        # global answer
        # global lookUp


        # first = (start + 0*hop, (start + 1 * hop) - 1)
        # second = ((start + 1 * hop), (start + 2 * hop) - 1)
        # third = ((start + 2 * hop), (start + 3 * hop) - 1)


    
    
    

def solution(N):

    for i in range(1, N):
        if 3 * (3 ** (i - 1) - 1) / 2 < N <= 3 * (3 ** i - 1) / 2:
            break
    
    start = (3 * (3 ** (i - 1) - 1) / 2) + 1
    end = (3 * (3 ** i - 1) / 2) + 1
    lookUp = {1: '1', 2: '2', 3: '4'}

    def realSolution(start, end, answer):

        if end - start < 3:
            return answer
    
        hop = (end - start) / 3
        for j in range(1, 4):
            if (start + (j - 1) * hop) <= N <= (start + j * hop) - 1:
                answer += lookUp[j]
                return realSolution(start + hop * (j - 1), end - (hop) * (3 - j), answer)

    return realSolution(start, end, '')

print(solution(37))
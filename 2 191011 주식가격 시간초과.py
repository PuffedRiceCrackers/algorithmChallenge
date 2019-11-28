

def solution(prices):
    answer = []
    for i in range(len(prices)):
        j = i
        while j <= len(prices) - 1 and prices[j] >= prices[i]:
            if j == len(prices) - 1:
                break
            else:
                j += 1
        answer.append(j - i)
    return answer
        
prices = [1, 2, 3, 2, 3]
print(solution(prices))
def solution(citations):
    if citations == [0]:
        return 0
    else:  
        citations.sort(reverse=True)
        for i in range(len(citations)):
            # h (citation[i]) 와 h이상 인용된 논문의 수 (i+1)를 비교
            if citations[i] == i + 1: 
                return citations[i]
            if citations[i] < i + 1:
                return i
        return len(citations)

citations = [3,3,3]
print(solution(citations))
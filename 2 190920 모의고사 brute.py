def solution(answers):
    supojas = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    rightAnswer = [0,0,0]

    for i in range(len(answers)):
        for j in range(len(supojas)):
            if answers[i] == supojas[j][i % len(supojas[j])]:
                rightAnswer[j] += 1

    return [i + 1 for i in range(len(rightAnswer)) if rightAnswer[i] == max(rightAnswer)]
    

#answers = [1, 2, 3, 4, 5]
answers = [1,3,2,4,2]
print(solution(answers))

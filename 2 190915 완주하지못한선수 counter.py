from collections import Counter

def solution(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)
    return (participant-completion).popitem()[0]

participant=['c', 'a', 'a', 'b']
completion = ['a', 'b', 'c']

print(solution(participant, completion))
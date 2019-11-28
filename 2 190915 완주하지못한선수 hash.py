
def solution(participant, completion):
    dictPart = {}
    hashSum = 0
    for person in participant:
        dictPart[hash(person)] = person
        hashSum += int(hash(person))
    for person in completion:
        hashSum -= hash(person)
    return dictPart[hashSum]

participant = ['a', 'a', 'a', 'b', 'c'] 
completion = ['a', 'a', 'b', 'c'] 

print(solution(participant, completion))
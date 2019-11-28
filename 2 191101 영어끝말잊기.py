


def solution(n, words):
    log = [[] for person in range(n)]
    for i in range(len(words)):
        if i > 0:
            if log[(i - 1) % n][-1][-1] != words[i][0] or words[i] in words[:i]:
                return [i % n + 1, len(log[i % n]) + 1]
        log[i % n].append(words[i])
    return [0, 0]
    

n = 2
words = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']
#words = ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']
#words = ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']
print(solution(n, words))
    

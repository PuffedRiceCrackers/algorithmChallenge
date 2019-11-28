from collections import deque

def returnDifference(word1, word2):
    difference = 0
    for alphabet1, alphabet2 in zip(word1, word2):
        if alphabet1 != alphabet2:
            difference += 1
    return difference

def findSeed(begin, words):
    seeds = {}
    for word in words:
        difference = returnDifference(begin, word)
        if difference == 0:
            seeds[word] = {"convertCount": 0}
        elif difference == 1:
            seeds[word] = {"convertCount": 1}
    return seeds

def createConnection(words):
    connectTable = {}
    for word in words:
        connectTable[word] = []
        for targetWord in words:
            difference = returnDifference(word, targetWord)
            if difference == 1:
                connectTable[word].append(targetWord)
    return connectTable

def solution(begin, target, words):
    seeds = findSeed(begin, words)
    if target not in words:
        return 0
    elif not seeds:
        return 0
    else:
        connTable = createConnection(words)     
        visited = {word: False for word in words}
        seedWords = seeds.keys()
        for seed in seedWords:
            queue = deque()
            queue.append((seed, seeds[seed]["convertCount"]))
            while queue:
                word, convertCount = queue.popleft()
                visited[word] == True
                if word == target:
                    return convertCount  # bfs 이므로 최초로 발견하였을 때가 min depth
                    # 사실 엄밀히 하면, 저 위에 seed 가 convertCount 오름차순으로 소팅되서 와야 되는데..
                for convertible in connTable[word]:
                    if visited[convertible] == False:
                        queue.append((convertible, convertCount + 1))              

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))


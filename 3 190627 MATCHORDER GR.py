import sys
sys.setrecursionlimit(1000000)

# Count win with given ratings
def calc(rusia, korea):
    if len(rusia) == 1:
        return rusia[0] <= korea[0] and 1 or 0

    # 'korea' was sorted : iterating from 0 gives the winning member with the min rating,
    for i in range(len(korea)):

        # A winning member exists -> remove that member
        if rusia[0] <= korea[i]: 
            del korea[i]
            del rusia[0]
            return 1 + calc(rusia, korea)  
        # A winning member does not exist -> remove memeber with smallest rating
        if i == len(korea) - 1:
            del korea[0]
            del rusia[0]
            return 0 + calc(rusia, korea)
        
tests = int(input())
for test in range(tests):
    numberOfMembers = int(input())
    rusiaRating = list(map(int, input().split()))
    koreaRating = list(map(int, input().split()))
    koreaRating.sort()
    print(calc(rusiaRating, koreaRating))
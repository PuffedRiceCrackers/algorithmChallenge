# -*- coding: utf-8 -*- 

minNum = int(input())
maxNum = int(input())
minPrime = maxNum+1
sumPrime = 0
result=[[num, -1] for num in range(maxNum+1)] 
 
''' result[x][1] = -1 아직탐색안함
    result[x][1] = 0  소수X
    result[x][1] = 1  소수O       '''

# result[0][], result[1][]은 편의상 안쓸것임
for seedNum in range(2,maxNum+1):
    
    # 소수임을 표시
    if result[seedNum][1] == -1:
        result[seedNum][1] = 1
        if seedNum >= minNum:
            sumPrime += seedNum
            if seedNum <= minPrime:
                minPrime = seedNum
    
    # seedNum의 크기에 따라, 배수해서 소수여부를 기록함
    if int(maxNum/seedNum) == 1 :
        continue
    for multiNum in range(2,int(maxNum/seedNum)+1):
        result[seedNum * multiNum][1]=0

# 소수의 합 인쇄 
if minPrime == maxNum + 1:
    print(-1)
else:
    print(sumPrime)
    
# 최소 소수 인쇄
if minPrime != maxNum + 1:
    print(minPrime)
    


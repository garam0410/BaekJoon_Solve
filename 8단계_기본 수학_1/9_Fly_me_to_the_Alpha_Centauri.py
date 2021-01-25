import math

case = int(input())

space = list()
result = list()

for i in range(0, case) : 
    space.append(input().split())

for i in range(0, case) : 
    distance = int(space[i][1]) - int(space[i][0])

    # 최소
    low = int(distance ** 0.5)

    #거리 합
    sum = 0

    #최소 횟수
    count = 2 * low - 1

    for j in range(1, low+1) : 
        sum += j
    
    sum *= 2
    sum -= low

    distance -= sum

    if distance == 0 : 
        pass
    else : 
        if distance % low > 0 : 
            count = count + distance // low + 1
        
        else :
            count = count + distance //low

    result.append(count)

for i in range (0,len(result)) : 
    print(result[i])


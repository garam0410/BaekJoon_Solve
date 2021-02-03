case = int(input())

result = list()

for i in range(0, case) : 
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    distance = ((abs(x2-x1))**2 + abs((y2-y1))**2)**0.5
    
    if x1 == x2 and y1 == y2 and r1 == r2: 
        result.append(-1)

    elif r1 + distance > r2 and r2 + distance > r1 and r1 + r2 > distance :
        result.append(2)
    
    elif r1 + distance == r2 or r2 + distance == r1 or r1 + r2 == distance : 
        result.append(1)
    
    else : result.append(0)

for i in range(0, len(result)) : 
    print(result[i])
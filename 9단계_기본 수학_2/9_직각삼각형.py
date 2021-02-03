result = list()

check = True

while check : 
    a, b, c = map(int, input().split())

    if a==0 and b==0 and c== 0 : 
        check = False
        break

    triangle = [a,b,c]

    looong = max(triangle)
    short = 0

    for i in range(0, 3) : 

        if triangle[i] == looong : pass
        
        else : 
            short += triangle[i]**2
    
    if looong**2 == short : 
        result.append('right')
    
    else : result.append('wrong')

for i in range(0, len(result)) : 
    print(result[i])
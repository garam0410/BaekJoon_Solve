import sys

case = sys.stdin.readline()

hotel = list()



people = 1

for i in range(0, int(case)) :
    get = list() 
    get.append(int(input()))
    get.append(int(input()))
    hotel.append(get)

for i in range(0, int(case)) : 
    result = list()
    people = 1
    for j in range(0, hotel[i][0]+1) : 
        
        ls = list()
        
        for k in range(0, hotel[i][1]+1) :    
            if j == 0: 
                ls.append(people)
                people += 1
            
            elif k == 0 : 
                ls.append(1)
            
            else : 
                num = result[j-1][k] + ls[k-1]
                ls.append(num)
            
        result.append(ls)
    
    print(result[hotel[i][0]][hotel[i][1]-1])
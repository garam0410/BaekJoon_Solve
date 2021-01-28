import sys

case = list()

out = list()

while True : 
    num = int(input())

    if num == 0 : 
        break

    else : 

        count = 0
        result = list()

        a = int((2*num) **0.5)

        for i in range(0, 2*num+1) : 
            result.append(True)
        
        for i in range(2, a+1) : 
            if result[i] == True : 
                for j in range(i+i, 2*num+1, i) : 
                    result[j] = False
        
        for i in range(num+1, 2*num+1) : 
            if result[i] == True : count +=1
        
        out.append(count)

for i in range(0, len(out)) : 
    print(out[i])
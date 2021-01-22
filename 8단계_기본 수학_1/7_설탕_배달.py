import sys

total = sys.stdin.readline()

sum = 0

result = list()

for i in range(0, int(total)//3 + 1) : 
    for j in range(0, int(total)//5 + 1) :     
        sum = 3*i + 5*j

        if int(total) == sum : 
            result.append(i+j)

if len(result) : 
    print(min(result))

else : print(-1)
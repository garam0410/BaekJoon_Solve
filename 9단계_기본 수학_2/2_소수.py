M = int(input())
N = int(input())

sum = 0
check = 0
minium = 0

for i in range(M, N+1) : 

    if i == 1 : continue

    for j in range(2, i) : 
        if i % j == 0 : 
            break

    else :
        sum += i

        if minium == 0 : 
            minium = i

if sum == 0 : 
    print(-1)

else : 
    print(sum)
    print(minium)
        

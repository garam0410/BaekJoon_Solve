num = int(input())

case = list(map(int, input().split()))

count = 0

for i in range(0,len(case)) : 

    check = 0

    if case[i] == 1 : continue

    elif 1 < case[i] < 4 : 
        count += 1

    else : 
        for j in range(2, case[i]) : 
            result = case[i] % j

            if result : continue
            else : check += 1
    
        if check == 0 : count +=1

print(count)

num = int(input())

case = list()
sosu = list()

output = list()

for i in range(0, num) : 
    case.append(int(input()))

for i in range(0, max(case)+1) : 
    sosu.append(True)

maximum = int(max(case)**0.5)

for i in range(2, maximum+1) : 
    if sosu[i] == True : 
        for j in range(2*i, max(case)+1, i) : 
            sosu[j] = False

for i in range(0, len(case)) : 

    value = case[i] //2

    if value == 2 : 
        print('2 2')
    
    else : 
        for j in range(value, 2, -1) : 
            if sosu[case[i] - j] ==  True and sosu[j] == True: 
                print(j, case[i] - j)
                break
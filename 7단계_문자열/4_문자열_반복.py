
count = int(input())
case = list()

for i in range(0, count) : 
    result= input().split()
    a = result[1]
    b = ''
    for j in range(0, len(a)) : 
        b += str(a[j] * int(result[0]))

    case.append(b)

for i in range(0, count) : 
    print(case[i])
num = 1

check = list()
self_num = list()

for i in range (0, 10000) : 
    check.append('')
    self_num.append('')

def d(num) : 
    result = 0

    if int(num) < 10 : 
        result += (num*2)
        check[result] = 0

    elif int(num) < 100:
        result = int(num) + int(num[0]) + int(num[1])
        check[result] = 0

    elif int(num) < 1000 : 
        result = int(num) + int(num[0]) + int(num[1]) + int(num[2])
        check[result] = 0
    
    elif int(num) < 10000 : 
        result = int(num) + int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])
        if result < 10000 : 
            check[result] = 0

for i in range (0, 10) : 
    d(i)

for i in range(10, 100) : 
    d(str(i))

for i in range(100, 1000) : 
    d(str(i))

for i in range(1000, 10000) : 
    d(str(i))

for i in range(0, 10000) : 
    if check[i] == '' : 
        print(i)
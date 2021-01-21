import math

case = int(input())

data = list()
result = list()

for i in range(0,case) : 
    data.append(input().split())


floor = 0
room = 0

for i in range(0, case) : 
    if int(data[i][2]) % int(data[i][0]) == 0 : 
        floor = int(data[i][0])
        room = int(data[i][2]) / int(data[i][0])
        print("%d" %(floor*100+room))
    else : 
        floor = int(data[i][2]) % int(data[i][0])
        room = math.ceil(int(data[i][2]) / int(data[i][0]))
        print("%d" %(floor*100+room))
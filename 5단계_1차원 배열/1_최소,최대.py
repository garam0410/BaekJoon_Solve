count = int(input())

num = input().split()

for i in range(0, count) : 
    num[i] = int(num[i])

max = num[0]
min = num[0]

for i in range(0, count) : 
    if num[i] > max :  
        max = num[i]
    
    elif num[i] < min : 
        min = num[i]

print(min, max)
 
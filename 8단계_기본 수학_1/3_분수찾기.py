num = int(input())

count = 0

result = 0

while result < num : 
    count +=1
    result = result + count

index = result - count

if count % 2 == 1 : 
    a = count - 1
    b = 0

    while index != num-1 : 
        a -= 1
        b += 1
        index += 1

    print("%d/%d"%(a+1,b+1))

elif count % 2 == 0 : 
    a = 0
    b = count - 1

    while index != num-1 : 
        a += 1
        b -= 1
        index += 1
    
    print("%d/%d"%(a+1,b+1))
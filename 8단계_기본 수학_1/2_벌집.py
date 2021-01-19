end = int(input())

i = 1
result = 1

result = result+6*i

if end == 1 : 
    print("1")

else : 
    while end > result : 
        i+=1
        result = result+6*i

    print(i+1)
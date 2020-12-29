count, num = input().split()

number = input().split(" ")
result = list()

for i in range(0, int(count)) : 
    if(int(number[i]) < int(num)) : 
        print(number[i], end=" ")
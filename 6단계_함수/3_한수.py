num = input()
count = 0

def function(num) :     
    if int(num) < 100 : 
        return True
    
    elif int(num) < 1000 : 
        if (int(num[1]) - int(num[0])) == (int(num[2]) - int(num[1])) : 
            return True

for i in range(1, int(num)+1) : 
    if function(str(i)) == True : 
        count += 1

print(count)
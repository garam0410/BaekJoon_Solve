count = int(input())

star = "*"
blank = " "
result = ""

for i in range(1, count+1) : 
    count = count-1
    result = result + blank*(count) + star*i
    print(result)
    result = ""
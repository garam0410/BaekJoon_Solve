cycle = 0

num = input()

if int(num) < 10 : 
    num += '0'

result = num[1] + str((int(num[0]) + int(num[1]))%10)

cycle += 1

while(result != num) : 
    result = result[1] + str((int(result[0]) + int(result[1]))%10)
    cycle += 1

print(cycle)
A, B = input().split()

result = list()

count = 0

while(A != '0' and B != '0') :
    result.append(A)
    result.append(B)
    A, B = input().split()
    count += 1

for i in range(0, count*2,2) : 
    print(int(result[i]) + int(result[i+1]))
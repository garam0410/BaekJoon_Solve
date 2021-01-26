N = int(input())

after_N = 0
result = list()

if N == 1 :
    pass
else : 
    for i in range(2, N+1) : 
        while N % i == 0 : 
            N = N/i
            result.append(i)

for i in range(0, len(result)) : 
    print(result[i])
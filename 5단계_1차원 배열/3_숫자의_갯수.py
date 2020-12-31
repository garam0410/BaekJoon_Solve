num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

count = [0,0,0,0,0,0,0,0,0,0]

result = num_1 * num_2 * num_3

result = str(result)

#len() : 크기 구하기
for i in range(0, len(result)) : 
    for j in range(0, 10) : 
        if result[i] == str(j) : 
            count[j] += 1

for i in range(0, 10) : 
    print(count[i])
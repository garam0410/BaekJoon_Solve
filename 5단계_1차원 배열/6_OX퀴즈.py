count = int(input())

score = list()

for i in range(0, count) : 
    score.append(0)

for i in range(0, count) : 
    result = input()

    k = 1

    for j in range(0, len(result)) : 
        if result[j] == 'O' : 
            if j == 0 : 
                score[i] += k
                k += 1

            else : 
                score[i] += k
                k+=1

        elif result[j] =='X' : 
            k = 1

for i in range(0, len(score)) : 
    print(score[i])
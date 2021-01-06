word = input()

result = list()
final_result = list()

for i in range(97, 124) : 
    result.append(i)
    final_result.append(-1)

for i in range(0, len(word)) : 
    for j in range(0, 27) : 
        if(result[j] == ord(word[i])) : 
            if final_result[j] == -1 :
                final_result[j] = i        

for i in range(0, 26) : 
    print(final_result[i], end=' ')
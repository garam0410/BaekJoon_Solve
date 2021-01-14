import sys

word = sys.stdin.readline().rsplit()

save_word = list()

for i in range(0, len(word)) : 

    sum_word = ""

    for j in range(2, -1, -1) : 
        sum_word += word[i][j]

    save_word.append(sum_word)

if save_word[0] > save_word[1] : 
    print(save_word[0])

else : 
    print(save_word[1])
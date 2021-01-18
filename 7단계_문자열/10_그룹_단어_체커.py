import sys

count = sys.stdin.readline().rstrip()

cnt = 0

word = list()

for i in range (0,int(count)) : 
    a = sys.stdin.readline().rstrip()
    word.append(a)

for i in range(0, len(word)) : 
    case = list()

    for j in range(0, len(word[i])) : 

        if case.count(word[i][j]) == 0 : 
            case.append(word[i][j])

        else : 

            if case[len(case)-1] == word[i][j] : 
                continue
        
            else : break

    else : cnt += 1

print(cnt)
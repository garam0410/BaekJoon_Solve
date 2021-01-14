import sys

word = sys.stdin.readline()

#인덱스는 다이얼 숫자, 값은 0부터 9까지 돌리는데 걸리는 시간
sec = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_alpha = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

result = 0

for i in range(2, 10) : 
    for j in range(len(num_alpha[i])) : 
        if word.count(num_alpha[i][j]) != 0 :
            result = result + (sec[i] * word.count(num_alpha[i][j]))

print(result)
subject_count = int(input())

score = input().split()

for i in range(0, len(score)) : 
    score[i] = int(score[i])

max = 0
result = 0

for i in range (0, subject_count) : 
    if score[i] > max : 
        max = score[i]

for i in range(0, subject_count) : 
    score[i] = score[i] / max * 100
    result += score[i]

print(result/subject_count)
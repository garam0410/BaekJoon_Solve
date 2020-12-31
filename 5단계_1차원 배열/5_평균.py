subject_count = int(input())

score = input().split()

max = 0

for i in range (0, subject_count) : 
    if score[i] > max : 
        max = score[i]

for i in range(0, subject_count) : 
    score[i] = score[i] / max * 100

print(score)
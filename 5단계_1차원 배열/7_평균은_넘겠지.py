import sys
case = int(input())

result = list()
sum = list()
percent = list()

for i in range(0,case) : 
    score = sys.stdin.readline().strip().rsplit()
    result.append(score)
    sum.append(0)
    percent.append(0)

i = 0
while i < case : 
    for j in range(0, int(result[i][0])) : 
        for k in range(1, int(result[i][0])+1) :
            #총점 계산
            sum[i] += int(result[j][k])
        
        #평균 계산
        sum[i] = sum[i] / int(result[i][0])

        #평균 넘는 학생 수 카운트
        for h in range(1, len(result[i])) : 
            if int(result[j][h]) > sum[i] : 
                percent[i] += 1
        
        #학생 수 비율 저장
        percent[i] = percent[i] / int(result[i][0])

        #다음 과목으로
        i += 1

for i in range(0, case) : 
    print("%.3f%%" %round(percent[i]*100,3))
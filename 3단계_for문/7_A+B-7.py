count = int(input())

num = list()

cnt = 1

for i in range(0, count) : 
    A, B = input().split()
    num.append(A)
    num.append(B)

for i in range(1, count*2+1, 2) : 

    if(cnt < count+1) : 
        print("Case #%d: %d" %(cnt,int(num[i-1]) + int(num[i])))
        cnt += 1
import sys

count = int(input())

num = list()

for i in range(0, count) : 
    A, B = sys.stdin.readline().rsplit()
    num.append(A)
    num.append(B)

for i in range(0, count*2, 2) : 
    print(int(num[i]) + int(num[i+1]))
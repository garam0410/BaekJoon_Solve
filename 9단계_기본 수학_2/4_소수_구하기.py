#에라토스테네스의 체

import sys

a, b = map(int,sys.stdin.readline().split())

result = list()

for i in range(0, b+1) : 
    result.append(True)

maximum = int(b**0.5)

for i in range(2, maximum+1) : 
    if result[i] == True : 
        for j in range(2*i, b+1, i) : 
            result[j] = False

for i in range(a, b+1) : 
    if result[i] == True and i != 1: 
        print(i)
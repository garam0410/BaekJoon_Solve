import math

a, b, v = map(int, input().split())

result = math.ceil((v-a)/(a-b)) + 1

if v - a < 0 : 
    print(1)

else :  print(result)
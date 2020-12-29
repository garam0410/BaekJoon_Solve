#숫자 입력
num1 = int(input())
num2 = int(input())

#자릿수 따오기
A = num2 // 100
B = (num2 - (A*100)) // 10
C = num2- (A*100) - (B*10)

#곱하기
print(num1*C)
print(num1*B)
print(num1*A)

print(num1 * num2)
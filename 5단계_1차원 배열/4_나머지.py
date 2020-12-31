number = list()

result = list()

for i in range(0, 10) : 
    num = input()
    number.append(int(num))

for i in range(0, 10) : 
    result.append(number[i]%42)

#자료형 set : 중복 허용 x, 내부 값들은 순서가 존재하지 않음
last_result = list(set(result))

print(len(last_result))
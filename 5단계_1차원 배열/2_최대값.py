number = list()

for i in range(0, 9) :
    num = input()
    number.append(int(num))

print(max(number))
print(number.index(max(number))+1)
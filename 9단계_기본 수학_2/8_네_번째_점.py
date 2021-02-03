x = list()
y = list()

rs_x = 0
rs_y = 0

for i in range(0, 3) : 
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(0, 3) : 
    if x.count(x[i]) == 1 : 
        rs_x = x[i]
        break

for i in range(0, 3) : 
    if y.count(y[i]) == 1 : 
        rs_y = y[i]
        break

print(rs_x, rs_y)
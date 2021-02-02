x, y, w, h = map(int, input().split())
result = {w-x,h-y, x,y}
print(min(result))
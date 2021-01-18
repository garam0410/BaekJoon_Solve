import sys

word = sys.stdin.readline().rstrip()

croatia = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')

for i in range(0, len(croatia)) : 
    word = word.replace(croatia[i], '*')
    
print(len(word))
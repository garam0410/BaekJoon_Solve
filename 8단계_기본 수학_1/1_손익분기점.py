A, B, C = map(int, input().split())

if B>C or B == C : 
    print("-1")

else : 
    print(A//(C-B) + 1)
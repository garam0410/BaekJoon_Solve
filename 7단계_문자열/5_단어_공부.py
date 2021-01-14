#upper() : 대문자화

word=input()
word=word.upper()

word_list=[]
for i in word:      #단어를 알파벳 중복 없이 리스트에 붙이기
    if i not in word_list:
        word_list.append(i)
 
count=0
word_count=[]   #각 알파벳이 입력받은 단어에 몇 번 나오는지 세기
for i in word_list:
    for j in word:
        if i==j:
            count+=1
    word_count.append(count)
    count=0    #각 알파벳마다 세고 count변수 초기화

a=max(word_count)
count2=0    
for i in word_count:    #가장 많이 나온 단어가 여러개인지 확인
    if i==a:
        count2+=1
if count2>1:
    print("?")
else:
    for i in range(len(word_count)):
        if word_count[i]==a:
            print(word_list[i])
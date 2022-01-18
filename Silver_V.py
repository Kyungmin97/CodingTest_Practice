"""n=int(input())
wlist=[]
for _ in range(n):
    word=input()
    wlist.append(word)
wlist2=wlist

for word in wlist2:
    sw=True
    for i in range(len(word)):
        for j in range(i,len(word)):
            print(word,word[i],word[j])
            if i == j:
                continue
            #print(word,word[i],word[j])
            if word[i] == word[j] and sw==True:
                wlist.remove(word)
                sw=False

print(len(wlist))
print(wlist)
"""

N = int(input())
result = N
for i in range(0,N):
    word=input()
    for j in range(0,len(word)-1):
        if word[j]==word[j+1]:
            continue
        if word[j] in word[j+1:]:
            result-=1
            break
print(result)


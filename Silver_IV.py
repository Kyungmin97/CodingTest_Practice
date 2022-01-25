"""
n=int(input())
nlist=list(map(int,input().split()))
count=n

for i in nlist:
    for j in range(2,i):
        if i/j == i//j:
            count-=1
            break
print(count-nlist.count(1))
"""


































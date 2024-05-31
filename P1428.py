n=int(input())
lst=input().split()
for i in range(0,n):
    ans=0
    for j in range(0,i):
        if int(lst[i])>int(lst[j]):
            ans+=1
    print(ans,end=' ')
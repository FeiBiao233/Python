n=int(input())
lst=input().split()
lst.append('0')
m=ans=1
for i in range(0,n):
    if int(lst[i])+1==int(lst[i+1]):
        ans+=1
        m=max(ans,m)
    else:
        ans=1
print(m)



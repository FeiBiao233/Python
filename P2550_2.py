sum=0
ans=[0 for i in range(1,9)]
l1=[0 for i in range(1,35)]
n=int(input())
num=[0]
num.extend(input().split())
num=[int(num[i]) for i in range(0,8)]
for i in range(1,8):
    l1[num[i]]=1
for i in range(1,n+1):
    num=[0]
    sum=0
    num.extend(input().split())
    num=[int(num[i]) for i in range(0,8)]
    for j in range(1,8):
        if l1[num[j]]==1:
            sum+=1
    ans[sum]+=1
ans=[str(ans[i]) for i in range(0,8)]
print(' '.join(ans[7:0:-1]))


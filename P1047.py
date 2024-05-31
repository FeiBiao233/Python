n,m=map(int,input().split())
ans=0
tree=[1 for i in range(0,n+1)]
for i in range(1,m+1):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        tree[j]=0
for i in range(0,n+1):
    if tree[i]==1:
        ans+=1
print(ans)
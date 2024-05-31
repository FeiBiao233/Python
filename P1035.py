k=int(input())
n,sum=0,0
while sum<=k:
    n+=1
    sum+=1/n
    if sum>k:
        break
print(n)
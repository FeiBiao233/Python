lst=list(map(int,input().split()))
sum=0
for i in range(0,len(lst)):
    sum+=lst[i]
print(sum*2**(len(lst)-1))
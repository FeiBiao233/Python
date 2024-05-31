def run(a):
    if a%100==0:
        if a%400==0:
            return 1
        else:
            return 0
    else:
        if a%4==0:
            return 1
        else:
            return 0
x,y=map(int,input().split())
lst=[]
ans=0
for i in range(x,y+1):
    if run(i):
        ans+=1
        lst.append(i)
print(ans)
for i in lst:
    print(i,end=' ')
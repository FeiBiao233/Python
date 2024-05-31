n,k=map(int,input().split())
num1,num2=0,0
ans1,ans2=0,0
for i in range(1,n+1):
    if i%k==0:
        ans1+=i
        num1+=1
    else:
        ans2+=i
        num2+=1
print(round(ans1/num1,1),round(ans2/num2,1))


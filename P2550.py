n=int(input())
sum=0
num=[0] #存放彩票或者中奖的
ans=[0 in range(1,9)]
l1=[0 for i in range(1,35)] #中奖数字标记
num.extend(input().split())
num=[int(num[i]) for i in range(1,8) ]
l1[num[1]]=l1[num[2]]=l1[num[3]]=l1[num[4]]=l1[num[5]]=l1[num[6]]=l1[num[7]]=1
for i in range(1,n+1):
    num=[0]
    sum=0
    num.extend(input().split())
    for j in range(1,8):
         if l1[num[j]]==1:
            sum+=1
    ans[sum]+=1
print(ans)
    

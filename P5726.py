n=int(input())
max,min,sum=-1,1000,0
num=input().split()
for i in range(0,n):
    if int(num[i])>=max:
        max=int(num[i])
    if min>=int(num[i]):
        min=int(num[i])
    sum+=int(num[i])
#num=[int(num[i]) for i in range(0,n)]
print(round((sum-max-min)/(n-2),2))
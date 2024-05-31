n=int(input())
sum=0
cheng=1
j=1
for i in range(1,n+1):
    cheng,j=1,1
    while j<=i:
        cheng*=j
        j+=1
    sum+=cheng
print(sum)
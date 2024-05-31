n=10000
sum=0
flag=1
num=[2,3,5,7,11,13,17]
for i in range(19,1200,2):
    flag=0
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            flag=1
    if flag==0:
        num.append(i)
        sum+=i
print(sum)
print(num)
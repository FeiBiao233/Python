n=int(input())
num=0
max=''
for i in range(0,n):
    temp=input()
    if len(temp)>len(max):
        max=temp
        num=i+1
    elif len(temp)==len(max):
        if temp>max:
            max=temp
            num=i+1
print(num)
print(max)

    
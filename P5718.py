min=10000
a=input()
lis=input().split()
for i in lis:
    if int(i)<=min:
        min=int(i)
print(min)

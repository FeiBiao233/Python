n=int(input())
set1=set()
set1.update(list(map(int,input().split())))
lst=sorted(set1)
print(len(lst))
for i in range(0,len(lst)):
    print(lst[i],end=' ')

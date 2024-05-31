n,m=map(int,input().split())
min=100000000
lst=[0]
if n==0:
    print(0)
    exit()
for i in range(1,n+1):
    lst.append(int(input()))
for i in range(1,n+2-m):
    for j in range(1,m):
        lst[i]+=lst[i+j]
    if(min>lst[i]):
        min=lst[i]
print(min)


'''这道题目的总结
第一，不要想当然，看清数据范围，我就是min开的太小了
第二，有一个加起来的，因为范例是3我就认为是3，结果不是
第三，小心反套路 比如最后的0 0
直接终结程序的办法 exit()'''
a,i,num='0',0,0
for i in range(100,1000):
    num=0
    str1=str(i)
    for a in str1:
        num+=int(a)**3
    if num==i:
        print(i)
def squ(x1,y1,x2,y2,l):
    if l==2:
        lst[x1][y1]=0
        return
    else:
        midx=int((x1+x2)/2)
        midy=int((y1+y2)/2)
        for i in range(x1,midx):
            for j in range(y1,midy):
                lst[i][j]=0
        squ(midx,y1,x2,midy,int(l/2))
        squ(x1,midy,midx,y2,int(l/2))
        squ(midx,midy,x2,y2,int(l/2))



n=int(input())
n=2**n
lst=[[1 for x in range(0,n)] for y in range(0,n)]
squ(0,0,n,n,n)
for i in range(0,n):
    for j in range(0,n):
        if j!=n-1:
            print(lst[i][j],end=' ')
        else:
             print(lst[i][j])
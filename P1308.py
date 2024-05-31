def str_find(s):
    ind=art.find(str,s,len(art))
    if ind==0 or ind+len(str)==len(art):
        return ind
    else:
        if art[ind-1]==' ' and art[ind+len(str)]==' ':
            return ind
        else:
            return str_find(ind+len(str)) 

ans=0
str=input().lower()
art=input().lower()
lst=art.split()
if str not in lst:
    print(-1)
else:
    for i in lst:
        if i==str:
            ans+=1
    print(ans,str_find(0))
    

#这道题我尽力了，python的效率太低，我没办法了    
#很神奇，自己电脑上面是错的，但是竟然洛谷就对了
#反正上面的就是正确代码

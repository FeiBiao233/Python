class stu:
    def __init__(self) -> None:
        self.name=''
        self.y=0
        self.m=0
        self.d=0
        self.num=0

from functools import cmp_to_key

def cmp(a,b):
    if a.y>b.y:
        return 1
    elif a.y<b.y:
        return -1
    else:
        if a.m>b.m:
            return 1
        elif a.m<b.m:
            return -1 
        else:
            if a.d>b.d:
                return 1
            elif a.d<b.d:
                return -1
            else:
                if a.num<b.num:
                    return 1
                else:
                    return -1

n=int(input())
lst=[]
for i in range(0,n):
    lst.append(stu())
    lst[i].name,lst[i].y,lst[i].m,lst[i].d=input().split()
    lst[i].y,lst[i].m,lst[i].d=int(lst[i].y),int(lst[i].m),int(lst[i].d)
lst.sort(key=cmp_to_key(cmp))
for i in range(0,n):
    print(lst[i].name)

#花了十分钟写完的代码，也算是默写结构体排序了，记住python缩进很重要

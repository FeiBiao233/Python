#先来一个不用高精度的,用结构体好了
class pri:
    def __init__(self) -> None:
        self.num=0
        self.sco=0

from functools import cmp_to_key
def cmp(a,b):
    if a.sco>b.sco:
        return -1
    else:
        return 1
n=int(input())
lst=[]
for i in range(0,n):
    lst.append(pri())
    lst[i].sco=int(input())
    lst[i].num=i+1
lst.sort(key=cmp_to_key(cmp))
print(lst[0].num)
print(lst[0].sco)
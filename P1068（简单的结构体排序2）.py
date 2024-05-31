class stu:
    def __init__(self) -> None:
        self.num=0
        self.sco=0

from functools import cmp_to_key

def cmp(a,b):
    if a.sco>b.sco:
        return -1
    elif a.sco<b.sco:
        return 1
    else:
        if a.num<b.num:
            return -1
        else:
            return 1

n,m=map(int,input().split())
lst=[]
for i in range(0,n):
    lst.append(stu())
    lst[i].num,lst[i].sco=map(int,input().split())
lst.sort(key=cmp_to_key(cmp))
ans=int(m*1.5)
while lst[ans-1].sco==lst[ans].sco:
    ans+=1
print(lst[ans-1].sco,ans)
for i in range(0,ans):
    print(lst[i].num,lst[i].sco)
#难点，重分.这道题的思路就是用while来算出最终重分的人数，然后再把人循环输出

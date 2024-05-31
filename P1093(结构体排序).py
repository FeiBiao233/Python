n=int(input())

class stu:
    def __init__(self):
        self.chi=0
        self.mat=0
        self.eng=0
        self.sco=0
        self.num=0

from functools import cmp_to_key

def cmp(a, b):
    if a.sco>b.sco:
        return -1
    elif a.sco<b.sco:
        return 1
    else:
        if a.chi>b.chi:
            return -1
        elif a.chi<b.chi:
            return 1
        else:
            if a.num<b.num:
                return -1
            else:
                return 1


lst=[]
for i in range(0,n):
    lst.append(stu())
    lst[i].num=i+1
    lst[i].chi,lst[i].mat,lst[i].eng=map(int,input().split())
    lst[i].sco=lst[i].chi+lst[i].mat+lst[i].eng
lst.sort(key=cmp_to_key(cmp))
for i in range(0,5):
    print(lst[i].num,lst[i].sco)
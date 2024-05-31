class stu:
    def __init__(self):
        self.chi=0
        self.mat=0
        self.eng=0
        self.sco=0
        self.num=0
        self.name=''

from functools import cmp_to_key

def cmp(a, b):
    if a.sco>b.sco:
        return -1
    elif a.sco<b.sco:
        return 1
    else:
        if a.num<b.num:
            return -1
        else:
            return 1

n=int(input())
lst=[]
for i in range(0,n):
    lst.append(stu())
    lst[i].num=i
    lst[i].name,lst[i].chi,lst[i].mat,lst[i].eng=input().split()
    lst[i].chi,lst[i].mat,lst[i].eng=int(lst[i].chi),int(lst[i].mat),int(lst[i].eng)
    lst[i].sco=lst[i].chi+lst[i].mat+lst[i].eng
lst.sort(key=cmp_to_key(cmp))
print(lst[0].name,lst[0].chi,lst[0].mat,lst[0].eng)
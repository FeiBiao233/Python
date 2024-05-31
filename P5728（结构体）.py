class stu:
    def __init__(self) :
        self.chi=0
        self.mat=0
        self.eng=0
        self.sco=0

n=int(input())
ans=0
lst=['0']
for i in range(1,n+1):
    lst.append(stu())
    lst[i].chi,lst[i].mat,lst[i].eng=map(int,input().split())
    lst[i].sco=lst[i].chi+lst[i].mat+lst[i].eng
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if abs(lst[i].chi-lst[j].chi)<=5 and abs(lst[i].mat-lst[j].mat)<=5 and abs(lst[i].eng-lst[j].eng)<=5 and abs(lst[i].sco-lst[j].sco)<=10:
            ans+=1
print(ans) 

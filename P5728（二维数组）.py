n=int(input())
lst=['0']
ans=0
for i in range(1,n+1):
    stu=['0']
    stu.extend(input().split())
    stu=[int(stu[j])for j in range(0,4)]
    stu[0]=stu[1]+stu[2]+stu[3]
    lst.append(stu)
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if abs(lst[i][1]-lst[j][1])<=5 and abs(lst[i][2]-lst[j][2])<=5 and abs(lst[i][3]-lst[j][3])<=5 and abs(lst[i][0]-lst[j][0])<=10:
            ans+=1
print(ans) 
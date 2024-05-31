k=int(input())
day,sum,num=0,0,0
while day<k:
    num=num+1
    if k>=day+num:
        sum+=num**2
        day+=num
    else:
        sum+=num*(k-day)
        break

print(sum)
'''w=(int(input()))/364
for i in range(1,101):
    if 1<=w-3*i<=100:
        print(int(w-3*i))
        print(i)
        break'''
# 以上是我自己写的代码，太耗时间了，下面有一个更加巧妙的方法

n=int(int(input())/364)
if n<=103:
    print(n-3)
    print(1)
else:
    if n%3==0:
        print(99)
        print(int((n-99)/3))
    if n%3==1:
        print(100)
        print(int((n-100)/3))
    if n%3==2:
        print(98)
        print(int((n-98)/3))
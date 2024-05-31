n=int(input())
i=2
while i<=pow(n,0.5):
    if n%i==0:
        print(int(max(i,n/i)))
    i+=1
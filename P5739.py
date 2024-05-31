def che(n):
    if n==1:
        return 1
    else:
        return n*che(n-1)
n=int(input())
print(che(n))
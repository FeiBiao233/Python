from functools import cmp_to_key

def cmp(a,b):
    if a+b>b+a:
        return -1
    else:
        return 1

n=int(input())
lst=input().split()
lst.sort(key=cmp_to_key(cmp))
print(''.join(lst[0:n]))

#这道题的核心在于这个cmp,粗粗的理解一下就是他永远能够保证是最后这个数字最大的str永远在前面，很不错，虽然是看了题解
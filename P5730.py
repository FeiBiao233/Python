n=int(input())
num=input()
l0=['XXX','X.X','X.X','X.X','XXX']
l1=['..X','..X','..X','..X','..X']
l2=['XXX','..X','XXX','X..','XXX']
l3=['XXX','..X','XXX','..X','XXX']
l4=['X.X','X.X','XXX','..X','..X']
l5=['XXX','X..','XXX','..X','XXX']
l6=['XXX','X..','XXX','X.X','XXX']
l7=['XXX','..X','..X','..X','..X']
l8=['XXX','X.X','XXX','X.X','XXX']
l9=['XXX','X.X','XXX','..X','XXX']
lst=[l0,l1,l2,l3,l4,l5,l6,l7,l8,l9]
for i in range(0,5):
    for j in num:
        print(lst[int(j)][i],end='.')
    print('\b ')

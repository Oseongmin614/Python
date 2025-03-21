n=int(input())
m=2
while(n>=m):
    if(n%m==0):
        print(m)
        n=n/m
    else:
        m+=1

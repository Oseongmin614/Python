sum=0
X=int(input())
N=int(input())
for _ in range(N):
    a,b=map(int,input().split())
    sum+=a*b
if sum==X:
    print("Yes")
else:
    print("No")
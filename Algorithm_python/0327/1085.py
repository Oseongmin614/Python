x1,y1,x2,y2=map(int,input().split())

x3=abs(x1-x2)
y3=abs(y1-y2)
print(min(x1,y1,x2,y2,x3,y3))
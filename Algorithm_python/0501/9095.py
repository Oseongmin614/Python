T = int(input())

for _ in range(T):
    n = int(input())
    co=[0,1,2,4]+[0]*n
    for i in range(4,n+1):
        co[i] = co[i-1]+co[i-2]+co[i-3]
    print(co[n])
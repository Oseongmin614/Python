

def div(n):
    arr=[]
    for i in range(1,int(n**(1/2))+1):
        if(n%i==0):
            arr.append(i)
            if((i**2) != n):
                arr.append(n//i)
    arr.sort()
    return arr

N,K = map(int,input().split())

arr = div(N)
if len(arr)>= K:
    print(arr[K-1])
else:
    print(0)

    N, K =map(int,input().split())
arr =[0]*N
j = 0
for i in range(1,N+1):
    if N%i == 0:
        j+=1
        arr[j]=i
print(arr[K])
N, K =map(int,input().split())
arr =[0]*N
j = 0
for i in range(1,N+1):
    if N%i == 0:
        j+=1
        arr[j]=i
print(arr[K])
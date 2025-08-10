N,K = map(int,input().split())
idx=0
arr=[]
arr_i=[]
for i in range(1,N+1):
    arr.append(i)

for _ in range(len(arr)):
    idx = (idx + K - 1) % len(arr)
    arr_i.append(arr.pop(idx))

print("<" + ", ".join(map(str, arr_i)) + ">")
N,K = map(int,input().split())
arr = [i for i in range(1,N+1)]
arr_2 = []
idx = 0

while arr:
    idx =(idx + K - 1) % len(arr)
    arr_2.append(arr.pop(idx))
    

print("<" + ", ".join(map(str, arr_2)) + ">")
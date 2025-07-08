n=int(input())
for i in range (n,0,-1):
    print("*" * ((i*2)-1))
    for j in range(n-i+1):
        print(" " , end="")
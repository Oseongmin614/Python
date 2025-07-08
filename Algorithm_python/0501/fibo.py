n= int(input())
mem = [0,1]+[-1]*(n-1)
def fibo(n):
    if (mem[n]==-1):
         mem[n] = fibo(n-1)+fibo(n-2)
    return mem[n]




print(fibo(n))
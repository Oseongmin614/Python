def pn(x):
    if x<2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

N = int(input())
j=0
arr= list(map(int,input().split()))
for i in arr:
    if pn(i):
        j+=1

print(j)
n= int(input())
M_sum=0
Y_sum=0
tamp=0
numbers = list(map(int, input().split()))
for i in range(n):
    tamp = numbers[i]//30
    Y_sum+=(tamp+1)*10
    M_sum+=((tamp//2)+1)*15

if Y_sum==M_sum:
    print("Y M",Y_sum)
elif Y_sum>M_sum:
    print("M",M_sum)
else:
    print("Y",Y_sum)

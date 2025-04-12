nums =0
min = 100
for i in range (7):
    a=int(input())
    if (a%2)==1:
        nums+=a
        if min>a:
            min=a

if nums == 0:
    print(-1)
else:
    print(nums)
    print(min)
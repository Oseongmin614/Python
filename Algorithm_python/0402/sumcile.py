N=int(input())
M=N
nums=[0,0,0]
i=0
while True:
    nums[0]=N//10
    nums[1]=N%10
    nums[2]=nums[0]+nums[1]
    N=nums[1]*10+(nums[2]%10)
    i+=1
    if N==M:
        print(i)
        break
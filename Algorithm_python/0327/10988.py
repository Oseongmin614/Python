str = input()
half = len(str)//2
stack=0
for i in range(half):

    if(str[i]==str[-(i+1)]):
        stack+=1
if(half==stack):
    print(1)
else:
    print(0)

str= input()
h =10
for i in range (1,len(str)):

    if str[i]==str[i-1]:
        h+=5
    else:
        h+=10
print(h)
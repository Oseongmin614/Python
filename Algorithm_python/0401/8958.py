T=int(input())

for _ in range(T):
    st = 0
    sum=0
    str=input()
    for i in range(len(str)):
        if str[i]=="O":
            if str[i-1] == "O":
                st+=1

            else:
                st=1

            sum+=st
        else:
            st=0

    print(sum)
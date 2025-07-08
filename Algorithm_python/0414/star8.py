N = int(input())
i_1=0
for i in range(1,2*N):
    if i > N:
        i_1 += 2
        i_2 =i-i_1
    else:
        i_2=i
    for j in range(i_2):
        print("*",end='')
    for k in range((N-i_2)*2):
        print(end=" ")
    for j in range(i_2):
        print("*", end='')
    if i != 2 * N - 1:
        print()
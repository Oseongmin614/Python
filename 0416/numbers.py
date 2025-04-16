A = int(input())
B = int(input())
C = int(input())
num = A*B*C
f_num = [0]*10

while num >0:
    i = num %10
    num//=10
    f_num[i]+=1
for j in range(10):
    print(f_num[j])
v=int(input())
pyo = input()
a_pyo = 0
b_pyo = 0
for i in range(0,v):
    if pyo[i]=='A':
        a_pyo+=1
    else:
        b_pyo+=1

if a_pyo>b_pyo:
    print("A")
elif b_pyo>a_pyo:
    print("B")
else:
    print("Tie")
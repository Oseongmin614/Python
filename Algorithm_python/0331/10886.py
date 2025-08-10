v=int(input())

a_pyo = 0
b_pyo = 0
for i in range(0,v):
    pyo = int(input())
    if pyo==1:
        a_pyo+=1
    else:
        b_pyo+=1

if a_pyo>=b_pyo:
    print("Junhee is cute!")
elif b_pyo>a_pyo:
    print("Junhee is not cute!")

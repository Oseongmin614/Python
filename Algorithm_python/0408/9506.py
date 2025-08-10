while True:
    numbers=[]
    n=int(input())
    if n==-1:
        break
    for i in range(1,n):
        if n %i==0:
            numbers.append(i)
    sum_numbers= sum(numbers)
    if sum_numbers == n:
        print(n, end=" = ")
        print(" + ".join(map(str, numbers)))
    else:
        print(n,"is NOT perfect.")
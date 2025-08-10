expr = input().split('-')

for i in range(0,len(expr)):
    if i ==0:
        answer=sum(map(int,expr[i].split('+')))
    else:
        answer -= sum(map(int, expr[i].split('+')))

print(answer)
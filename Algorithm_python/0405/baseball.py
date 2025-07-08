T=int(input())
for _ in range(T):
    y_t=0
    k_t=0
    for _ in range(9):
        y,k=map(int,input().split())
        y_t+=y
        k_t+=k
        
    if y_t > k_t:
        print("Yonsei")
    elif k_t > y_t:
        print("Korea")
    else:
        print("Draw")
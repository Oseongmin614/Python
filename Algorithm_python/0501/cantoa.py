def cantoa(N):
    if N==1:
        return "-"
    M = N//3
    side = cantoa(M)
    center = " " * M
    return side + center +side

while True:
    try:
        N=int(input())
        print(cantoa(3**N))

    except EOFError:
        break
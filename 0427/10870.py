def fivo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return fivo(N-1)+fivo(N-2)

N= int(input())
print(fivo(N))
        
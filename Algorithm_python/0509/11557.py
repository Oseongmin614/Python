N= int(input())
for _ in range(N):
    S = int(input())
    max_name = ''
    max_l = 0
    for _ in range(S):
        name, l = input().split()
        l = int(l)
        if max_l < l:
            max_l = l
            max_name = name
    print(max_name)
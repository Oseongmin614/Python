#r은 광고를 하지 않았을 때 수익
# e는 광고를 했을 때의 수익,
#c는 광고 비용
i=int(input())
for _ in range(i):
    r,e,c = map(int,input().split())
    if r==e-c:
        print("does not matter")
    elif r>e-c:
        print("do not advertise")
    else:
        print("advertise")
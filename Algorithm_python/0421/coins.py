N,K = map(int,input().split())
coinlist =[]
coins =0
for _ in range(N):
    coinlist.append(int(input()))


while K>0:

    if K > coinlist[N]:
        coins += K//coinlist[N]
        K %= coinlist[N]
    N -= 1
print(coins)


N, K = map(int, input().split())
coinlist = [int(input()) for _ in range(N)]

coins = 0
idx = N - 1

while K > 0 and idx >= 0:
    if K >= coinlist[idx]:
        coins += K // coinlist[idx]
        K %= coinlist[idx]
    idx -= 1

print(coins)
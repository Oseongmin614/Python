
num_list_a = []
num_list_b = []
N, M = map(int, input().split())



for i in range(N):
        num_list_a[i].append(int, input().split())

for i in range(N):
        num_list_b[i].append(int, input().split())


result = [[0]*M for _ in range(N)]
for i in range(N):
        for j in range(M):
                result[i][j] = num_list_a[i][j] + num_list_b[i][j]


for row in result:
        print(' '.join(map(str, row)))

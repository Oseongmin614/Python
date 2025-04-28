import sys
N = int(input())
arr =[]
for _ in range(N):
    arr.append(sys.stdin.readline().strip())

arr.sort(key=lambda x: int(x[0]))

for i in range (len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end=" ")
    print()
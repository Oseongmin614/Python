import sys
N = int(input( ))
arr = set()

for _ in range(N):
    arr.add(sys.stdin.readline().strip())

arr = list(arr)
arr.sort()
arr.sort(key = len)

for i in arr:
    print(i)

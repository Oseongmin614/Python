import sys
n=int(input())
li=[]
for i in range(n):
    
    li.append(list(map(int, sys.stdin.readline().split())))
li.sort()
for i in li:
    print(i[0], i[1])
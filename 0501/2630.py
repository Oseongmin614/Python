import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white = 0
blue = 0

def cut(x, y, n):
    global white, blue
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                half = n // 2
                cut(x, y, half)
                cut(x, y + half, half)
                cut(x + half, y, half)
                cut(x + half, y + half, half)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

cut(0, 0, N)
print(white)
print(blue)
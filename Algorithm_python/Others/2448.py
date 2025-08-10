def draw_star(n, x, y):
    if n == 3:
        star[x][y] = '*'
        star[x + 1][y - 1] = '*'
        star[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            star[x + 2][y + i] = '*'
    else:
        draw_star(n // 2, x, y)
        draw_star(n // 2, x + n // 2, y - n // 2)
        draw_star(n // 2, x + n // 2, y + n // 2)

N = int(input())
star = [[' '] * (2 * N) for _ in range(N)]
draw_star(N, 0, N - 1)

for row in star:
    print(''.join(row))
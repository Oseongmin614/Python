def solution(ineq, eq, n, m):
    if ineq == "<":
        return 1 if (n <= m if eq == "=" else n < m) else 0
    else:
        return 1 if (n >= m if eq == "=" else n > m) else 0
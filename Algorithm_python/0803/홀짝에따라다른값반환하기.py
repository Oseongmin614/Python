def solution(n):
    if n % 2 == 1:
        count = (n + 1) // 2
        return count * count
    else:
        return sum(i*i for i in range(2, n+1, 2))
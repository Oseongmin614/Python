def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b, c):
    a//= c
    b //= c
    c*=b*a
    return c

n,m= map(int,input().split())
divsor = gcd(n,m)
multiple = lcm(n,m,divsor)

print(divsor)
print(multiple)

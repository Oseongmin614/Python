from math import gcd, isqrt

n = int(input())
numbers = list(map(int, input().split()))

if n == 2:
    g = gcd(numbers[0], numbers[1])
else:
    g = gcd(numbers[0],gcd(numbers[1],numbers[2]))


result = set()
for i in range(1, isqrt(g) + 1):
    if g % i == 0:
        result.add(i)
        result.add(g // i)
for num in sorted(result):
    print(num)
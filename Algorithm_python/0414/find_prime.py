N = input()
M = 0
nums = list(map(int, input().split()))

def pn(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

for j in nums:
    if pn(j):
        M += 1
print(M)
i = int(input())
num = int(input())
sum =0
while num >= 10:
    sum += num % 10
    num //=10
sum += num
print(sum)

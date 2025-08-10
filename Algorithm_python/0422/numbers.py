N, M = map(int, input().split())
numbers = list(map(int, input().split()))

cnt = 0
start = 0
end = 0
current_sum = 0

while True:
    if current_sum >= M:
        current_sum -= numbers[start]
        start += 1
    elif end == N:
        break
    else:
        current_sum += numbers[end]
        end += 1

    if current_sum == M:
        cnt += 1

print(cnt)
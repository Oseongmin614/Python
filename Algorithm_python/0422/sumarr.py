import sys

input = sys.stdin.readline

N, M = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

ap, bp = 0, 0
answer = []

while ap < N and bp < M:
    if a_list[ap] <= b_list[bp]:
        answer.append(a_list[ap])
        ap += 1
    else:
        answer.append(b_list[bp])
        bp += 1

answer += a_list[ap:]
answer += b_list[bp:]

print(' '.join(map(str, answer)))

i=int(input())
answer = "int"
for _ in range(i//4):
    answer="long "+answer

print(answer)
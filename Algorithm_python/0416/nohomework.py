students = [0]*30

for _ in range(28):
    i=int(input())
    students[i-1]=1

missing = [i + 1 for i, v in enumerate(students) if v == 0]

print(missing[0])
print(missing[1])
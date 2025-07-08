t = int(input())
for k in range(t):
    i, str_input = input().split()
    i = int(i)
    result = ""
    for letter in str_input:
        result += letter * i
    print(result)
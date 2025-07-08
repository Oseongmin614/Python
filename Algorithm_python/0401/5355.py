T = int(input())

for i in range(T):
    inputs = input().split()
    result = float(inputs[0])
    for j in range(1, len(inputs)):
        if inputs[j] == "@":
            result *= 3
        elif inputs[j] == "%":
            result += 5
        elif inputs[j] == "#":
            result -= 7
    print("{:.2f}".format(result))
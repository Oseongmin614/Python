X = int(input())
print("ㄱㄷ")
stick = 64
stack=0
stick_len =0
while X!=stick_len:
    if X<stick:
        stick //= 2
    print(stick)
    stack += 1
    stick_len += stick
print(stack)
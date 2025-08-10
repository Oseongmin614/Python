str = "WelcomeToSMUPC"
N = int(input())
while N>len(str):
    N=N-len(str)

print(str[N-1])
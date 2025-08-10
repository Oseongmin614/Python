N = int(input())
mimlist = [
    'Never gonna give you up',
    'Never gonna let you down',
    'Never gonna run around and desert you',
    'Never gonna make you cry',
    'Never gonna say goodbye',
    'Never gonna tell a lie and hurt you'
]

is_valid = True
for _ in range(N):
    text = input()
    if text not in mimlist:
        is_valid = False
        break

if is_valid:
    print("No")
else:
    print("Yes")
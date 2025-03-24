a = int(input())
words = []

for i in range(a):
    str_input = input()
    words.append(str_input.split())

reversed_words = [' '.join(reversed(sentence)) for sentence in words]
print(""+reversed_words)
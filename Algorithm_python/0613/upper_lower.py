def solution(my_string):
    answer = []
    for c in my_string:
        if c.islower():
            answer.append(c.upper())
        else:
            answer.append(c.lower())
    return ''.join(answer)
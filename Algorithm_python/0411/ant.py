def solution(hp):
    answer = 0
    ant = 5
    while hp != 0:
        answer += hp // ant
        hp %= ant
        ant -= 2
    return answer
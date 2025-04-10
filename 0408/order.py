def solution(emergency):
    sorted_em = sorted(emergency, reverse=True)
    answer = [sorted_em.index(i) + 1 for i in emergency]
    return answer
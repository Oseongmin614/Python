def solution(n, control):
    return sum(({'w':1,'s':-1,'d':10,'a':-10}[c] for c in control), n)

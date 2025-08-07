def solution(a,b,c,d):
    from collections import Counter
    v,cnt = zip(*Counter([a,b,c,d]).items())
    if len(v)==1:return 1111*v[0]
    if 3 in cnt:
        p,q = v[cnt.index(3)],v[cnt.index(1)]
        return (10*p+q)**2
    if cnt.count(2)==2:return (v[0]+v[1])*abs(v[0]-v[1])
    if 2 in cnt:
        p = v[cnt.index(2)]
        q,r = [x for x in v if x!=p]
        return q*r
    return min(a,b,c,d)

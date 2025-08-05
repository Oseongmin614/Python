def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        candidates = [x for x in arr[s:e+1] if x > k]
        if candidates:
            answer.append(min(candidates))
        else:
            answer.append(-1)
    return answer
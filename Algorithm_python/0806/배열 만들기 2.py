def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        num_str = str(num)
        if all(ch in ['0', '5'] for ch in num_str):
            answer.append(num)
    if not answer:
        return [-1]
    return answer
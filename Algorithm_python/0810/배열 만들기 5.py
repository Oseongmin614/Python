def solution(intStrs, k, s, l):
    answer = []
    for str_num in intStrs:
        num = int(str_num[s:s+l])
        if num > k:
            answer.append(num)
    return answer
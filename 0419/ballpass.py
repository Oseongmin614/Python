def solution(numbers, k):
    j = 0    
    for i in range(k-1):
        j += 2
        if len(numbers) <= j:
            j-=len(numbers)

    return numbers[j]
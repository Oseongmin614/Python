def solution(numbers, k):
    index = 0
    for i in range(k-1):
        index += 2
        if len(numbers) <= index:
            index-=len(numbers)

    return numbers[index]
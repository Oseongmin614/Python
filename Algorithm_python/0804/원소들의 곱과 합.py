def solution(num_list):
    total_sum = sum(num_list)
    product = 1
    for num in num_list:
        product *= num
    
    return 1 if product < total_sum ** 2 else 0
def solution(num_list):
    odd = ''.join(str(x) for x in num_list if x % 2 == 1)
    even = ''.join(str(x) for x in num_list if x % 2 == 0)
    odd_num = int(odd) if odd else 0
    even_num = int(even) if even else 0
    return odd_num + even_num
fs = input()
ft = input()


temp = True
fs_index = 0
ft_index = 0

while fs_index < len(fs) * len(ft) and ft_index < len(ft) * len(fs):
    if fs[fs_index % len(fs)] != ft[ft_index % len(ft)]:
        temp = False
        break
    fs_index += 1
    ft_index += 1

print(1 if temp else 0)
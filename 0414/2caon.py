nums = [1, 2, 3, 4, 5, 6]
answer = []

for i in range(0, len(nums), 3):
    answer.append([nums[i], nums[i+1]])

print(answer)
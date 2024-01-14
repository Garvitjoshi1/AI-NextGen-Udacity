# nums = [1, 1, 4, 2, 3, 2, 5, 5, 5, 7]
nums = [15]
dictionary = {}
count = 0
nums.sort()
for i in range(0, len(nums) - 1):
    if nums[i] == nums[i + 1]:
        count += 1
        dictionary.__setitem__(nums[i], count)
print(dictionary)
print(nums)

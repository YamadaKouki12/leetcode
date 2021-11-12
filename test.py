

nums = [3,4,5]
target=9
dict = {}
for i in range(len(nums)):
    if target - nums[i] not in dict:
        dict[nums[i]] = i
    else:
        print([i, dict[nums[i]]])
print(0)

def twoSum(nums, target):
    seen_map = {}
    for ind, num in enumerate(nums):
        comp = target - num
        if comp in seen_map:
            return [seen_map[comp], ind]
        seen_map[num] = ind

    return []

print(twoSum(nums = [3,4,5,6], target = 7))
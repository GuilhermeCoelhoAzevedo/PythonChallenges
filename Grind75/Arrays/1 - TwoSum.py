#https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
    d = {}

    for i, e in enumerate(nums):
        if target - e in d:
            return [d[target - e], i]
        else:
            d[e] = i

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))
#https://leetcode.com/problems/majority-element/description/

from collections import Counter

def majorityElement(nums):
    counter = Counter(nums)
    return counter.most_common(1)[0][0]

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))

#Optimized solution
"""
def majorityElement(nums):
    nums.sort()
    n = len(nums)
    return nums[n // 2]
"""
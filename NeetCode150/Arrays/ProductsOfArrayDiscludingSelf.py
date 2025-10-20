#https://neetcode.io/problems/products-of-array-discluding-self

import math

def productExceptSelf(nums):
    n = len(nums)
    result = []

    for i in range(n):
        result.append(math.prod(nums[0:i] + nums[i+1:]))

    return result

nums = [1,2,4,6]

print(productExceptSelf(nums))

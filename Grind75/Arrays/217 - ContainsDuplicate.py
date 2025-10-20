#https://leetcode.com/problems/contains-duplicate/description/

def containsDuplicate(nums):
    num_set = set()

    for n in nums:
        if n in num_set:
            return True
        else:
            num_set.add(n)

    return False

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))
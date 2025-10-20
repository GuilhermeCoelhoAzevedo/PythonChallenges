#https://leetcode.com/problems/missing-number

def find_missing(nums):
    count = 0
    nums.sort()

    for num in nums:
        if num == count:
            count+=1
        else:
            return count

    return count

nums = [9,6,4,2,3,5,7,0,1]
print(find_missing(nums))
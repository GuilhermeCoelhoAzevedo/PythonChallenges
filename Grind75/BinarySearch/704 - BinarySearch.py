#https://leetcode.com/problems/binary-search/description/

def search(nums : list[int], target : int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        # Finding the mid using floor division
        index = left + (right - left) // 2

        # Target value is present at the middle of the array
        if nums[index] == target:
            return index
        # Target value is present in the high subarray
        elif nums[index] < target:
            left = index + 1
        # Target value is present in the low subarray
        else:
            right = index - 1

    return -1

nums = [-1,0,3,5,9,12]
target = 0

print(search(nums, target))
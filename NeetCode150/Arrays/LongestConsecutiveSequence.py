#https://neetcode.io/problems/longest-consecutive-sequence

#Solution using hashSet
def longestConsecutive(nums):
    #Edge case
    if not nums:
        return 0

    numSet = set(nums)
    result = 0

    for num in numSet:
        #Look for first number in sequences
        if num - 1 not in numSet:
            #Calculates length of sequence
            length = 1
            while num + length in numSet:
                length += 1

            # Saves maximum length found
            result = max(result, length)

    return result

nums = [0,3,2,5,4,6,1,1]
#nums = [1,3]
print(longestConsecutive(nums))

#Solution using sorting
"""
def longestConsecutive(nums):
    #Edge case
    if not nums:
        return 0

    #Taking out duplicate numbers and sorting the array
    nums = list(set(nums))
    nums.sort()

    length = 1
    result = 1

    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] == 1:
            length +=1
            result = max(result, length)
        else:
            length = 1

    return result
"""
#https://leetcode.com/problems/two-sum

def two_sum(nums, target):
    d = {}
    for index, e in enumerate(nums):
        if target - e in d.keys():
            return [d[target - e], index]
        else:
            d[e] = index

        index +=1

nums = [3,2,4]
target = 6
print(two_sum(nums, target))


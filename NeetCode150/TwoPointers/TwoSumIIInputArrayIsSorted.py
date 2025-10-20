def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        curSum = numbers[left] + numbers[right]

        #If total is bigger than target, decrease right index to get smaller total
        if curSum > target:
            right -= 1
        # If total is smaller than target, increase left index to get bigger total
        elif curSum < target:
            left +=1
        #Return indexes that sum up to target
        else:
            return [left + 1, right + 1]

    return []

numbers = [1,2,3,4,5,6,7]
target = 7

print(twoSum(numbers, target))
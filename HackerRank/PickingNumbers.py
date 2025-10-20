def pickingNumbers(a):
    numbers = set(a)
    max_subarray = 0

    for item in numbers:
        num1 = a.count(item)
        num2 = a.count(item - 1)

        if num1 + num2 > max_subarray:
            max_subarray = num1 + num2

    return max_subarray

a = [4,6,5,3,3,1]
print(pickingNumbers(a))
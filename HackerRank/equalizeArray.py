def equalizeArray(arr):
    d = {}
    max_value = 0

    for e in arr:
        if e in d:
            d[e] += 1
        else:
            d[e] = 1

        if d[e] > max_value:
            max_value = d[e]

    return len(arr) - max_value

arr =  [3,3,3,2,2]
print(equalizeArray(arr))

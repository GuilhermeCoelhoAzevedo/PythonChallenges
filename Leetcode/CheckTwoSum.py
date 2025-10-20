def check_two_sum(arr, t):
    d = {}

    for e in arr:
        if t - e in d.keys():
            return True
        else:
            d[e] = e

    return False

arr = [5,7,1,2,8,4,3]
t = 19
print(check_two_sum(arr, t))


#https://neetcode.io/problems/single-number

from collections import defaultdict, Counter

def singleNumber(nums):
    return Counter(nums).most_common()[-1][0]

nums = [3,2,2,3, 4]
print(singleNumber(nums))

#Answer creating dictionary manually
"""
    d = defaultdict(int)

    for n in nums:
        d[n] += 1

    return min(d.keys(), key=d.get)
"""
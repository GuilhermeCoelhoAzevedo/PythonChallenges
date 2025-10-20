#https://neetcode.io/problems/top-k-elements-in-list

from collections import Counter, defaultdict

def topKFrequent(nums, k):
    counter = Counter(nums).most_common(k)
    result = []

    for v, f in counter:
        result.append(v)

    return result


nums = [1,2,2,3,3,3]
k = 2

print(topKFrequent(nums, k))

#Question with more development
"""
def topKFrequent(nums, k):
    frequency = defaultdict(int)

    for n in nums:
        frequency[n] +=1

    arr = []
    for num, count in frequency.items():
        arr.append([count, num])
    arr.sort()

    result = []

    while len(result) < k:
        result.append(arr.pop()[1])

    return result
"""
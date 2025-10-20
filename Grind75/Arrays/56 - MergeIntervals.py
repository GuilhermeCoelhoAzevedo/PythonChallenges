#https://leetcode.com/problems/merge-intervals/description

def merge(intervals):
    #Adds new interval and sorts the array
    intervals.sort()

    result = []

    for interval in intervals:
        #Add first interval if result is empty
        if not result:
            result.append(interval)
            continue

        #Check and solves overlaps
        previous = result[-1]
        if interval[0] in range(previous[0], previous[1] + 1):
            result[-1] = [min(previous[0], interval[0]), max(previous[1], interval[1])]
        else:
            result.append(interval)

    return result

intervals = [[1,3],[2,6],[8,10],[15,18]]
newInterval = [3,6]

print(merge(intervals))

#https://leetcode.com/problems/insert-interval/description

def insert(intervals, newInterval):
    #Adds new interval and sorts the array
    intervals.append(newInterval)
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

intervals = [[2,4],[5,7],[8,10],[11,13]]
newInterval = [3,6]

print(insert(intervals, newInterval))

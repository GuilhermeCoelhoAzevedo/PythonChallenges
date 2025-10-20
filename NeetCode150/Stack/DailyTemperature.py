#https://neetcode.io/problems/daily-temperatures

def dailyTemperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)

    for i, t in enumerate(temperatures):
        #Removes lower temperatures from stack
        while stack and t > stack[-1][1]:
            stackI = stack.pop()[0]
            #Calculate days difference using indexes
            result[stackI] = i - stackI

        #Add temperature to the stack
        stack.append((i, t))

    return result

temperatures = [30,38,30,36,35,40,28]
print(dailyTemperatures(temperatures))

#Brute force - (n^2)
"""
def dailyTemperatures(temperatures):
    result = [0] * len(temperatures)

    for t in range(len(temperatures) - 1):
        for t2 in range(t + 1, len(temperatures)):
            if temperatures[t] < temperatures[t2]:
                result[t] = t2 - t1
                break

    return result
"""
def birthdays(s, d, m):
    count = 0

    for i in range(len(s)):
        #If it's not possible to create new sizes, stop the process
        if i+m > len(s):
            break

        #Check if portion equal requested
        if sum(s[i:i+m]) == d:
            count+=1

    return count

s = [1,1,1]
d = 3
m = 3

print(birthdays(s, d, m))
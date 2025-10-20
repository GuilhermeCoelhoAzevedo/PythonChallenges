def countingValleys(steps, path):

    count = 0
    valleys = 0

    for step in path:
        if step == "U":
            if count == -1:
                valleys += 1

            count +=1
            continue

        count -=1

    return valleys

steps = 8
path = "UDDDUDUU"

print(countingValleys(steps, path))
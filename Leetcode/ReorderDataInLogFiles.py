#https://leetcode.com/problems/reorder-data-in-log-files

def reorderLogFiles(logs):
    digit_logs = []
    letter_logs = []

    for log in logs:
        split_log = log.split()
        if split_log[1].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(log)

    letter_logs.sort(key=lambda x: x.split()[0])
    letter_logs.sort(key=lambda x: x.split()[1:])

    return letter_logs + digit_logs

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
print(reorderLogFiles(logs))


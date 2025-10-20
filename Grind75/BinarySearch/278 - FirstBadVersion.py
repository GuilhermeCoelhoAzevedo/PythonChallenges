#https://leetcode.com/problems/first-bad-version/description

bad = 4

def isBadVersion(version: int) -> bool:
    if version >= bad:
        return True
    else:
        return False

def firstBadVersion(n) -> int:
    left, right = 1, n

    while left < right:
        version = left + (right - left) // 2

        if isBadVersion(version):
            right = version
        else:
            left = version + 1

    return left

n = 5 #[1, 2, 3, 4, 5]
print(firstBadVersion(n))
#https://leetcode.com/problems/climbing-stairs/description

def climbStairs(n) -> int:
    if n == 0 or n == 1:
        return 1

    return climbStairs(n - 1) + climbStairs(n - 2)

n = 4
print(climbStairs(n))


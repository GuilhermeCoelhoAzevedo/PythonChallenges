def numIslands(grid):
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == "0":
                continue

            if r - 1 >= 0:
                if grid[r-1][c] == "1":
                    continue

            if c - 1 >= 0:
                if grid[r][c-1] == "1":
                    continue

            count +=1

    return count

"""
grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
        ]
"""
"""
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
"""
grid = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]



print(numIslands(grid))
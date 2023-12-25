class Solution:
    def uniquePaths(self, grid):
        if not grid or not grid[0]:
            return 0

        r, c = len(grid), len(grid[0])

        # If start or end is off-limits, return 0
        if grid[0][0] == False or grid[r-1][c-1] == False:
            return 0

        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[0][0] = 1

        # Fill the dynamic programming table
        for i in range(r):
            for j in range(c):
                if grid[i][j]:  # Only proceed if the cell is not off-limits
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1]

        
        return dp[r-1][c-1]

# Example usage
grid = [
    [True, True, True],
    [True, False, True],
    [True, True, True]
]
solution = Solution()
print("minimum grid cost is ", solution.uniquePaths(grid))

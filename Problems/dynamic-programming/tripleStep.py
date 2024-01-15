"""A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs."""

class Solution:
    memo = {}
    def tripleStepTopDown(self, n):
        if n in self.memo:
            return self.memo[n]
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            ret = self.tripleStepTopDown(n-1) + self.tripleStepTopDown(n-2) + self.tripleStepTopDown(n-3)
            self.memo[n] = ret
            return ret


     # Bottom up (more optimised solution with O(1) space)
    def tripleStep(self, n):
        if n < 0:
            return 0
        elif n == 0:
            return 1

        memo = [0] * (n + 1)
        memo[0], memo[1] = 1, 1
        if n >= 2:
            memo[2] = 2

        for i in range(3, n + 1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

        return memo[n]

solution = Solution()
print(solution.tripleStepTopDown(100))
print(solution.tripleStep(1000))
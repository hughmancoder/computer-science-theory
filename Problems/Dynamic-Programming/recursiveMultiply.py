class Solution:
    memo = {}
    def multiply(self, a, b):
        self.memo = {}
        if a < b:
            return self.recursiveMultiply(a, b)
        else:
            return self.recursiveMultiply(b, a)

    def recursiveMultiply(self, a, b):
        if a == 0 or b == 0:
            return 0
        elif a == 1:
            return b
        elif (a, b) in self.memo:
            return self.memo[(a, b)]
        
        if b % 2 == 0:
            res = self.recursiveMultiply(a, b // 2) << 1
        else:
            res = a + (self.recursiveMultiply(a, b // 2) << 1)
        
        self.memo[(a, b)] = res
        return res


solution = Solution()
a = 23432423
b = 2432232
print(solution.multiply(a,b) == a * b)

a = 0
b = 2432
print(solution.multiply(a,b) == a * b)

a = -32
b = 432
print(solution.multiply(a,b) == a * b)



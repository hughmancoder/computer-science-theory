class Solution:
    memo = {}
    def multiply(self,a, b):
        self.memo = {}
        A = abs(a)
        B = abs(b)
        if A < B:
            res =  self.recursiveMultiplyV2(A, B)
        else:
            res = self.recursiveMultiplyV2(B, A)
        
        if(a < 0 and b > 0) or (a > 0 and b < 0):
            return -res
        return res

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
    
    def recursiveMultiplyV2(self, smaller, bigger):
        if smaller == 0:
            return 0
        elif smaller == 1:
            return bigger

        if smaller in self.memo:
            return self.memo[smaller]

        s = smaller >> 1 # divide by 2
        halfProd = self.recursiveMultiplyV2(s, bigger)

        if smaller % 2 == 0:
            result = halfProd << 1
        else:
            result = (halfProd << 1) + bigger

        self.memo[smaller] = result
        return result
        

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



class Solution:
    def findMagicIndexDistinct(self, A):
        return self.binarySearchDistinct(A, 0, len(A) - 1)

    def binarySearchDistinct(self, A, start, end):
        if start > end:
            return -1

        mid = start + (end - start) // 2
        if A[mid] == mid:
            return mid
        elif A[mid] > mid:
            return self.binarySearchDistinct(A, start, mid - 1)
        else:
            return self.binarySearchDistinct(A, mid + 1, end)

    def findMagicIndexNonDistinct(self, A):
        return self.searchNonDistinct(A, 0, len(A) - 1)

    def searchNonDistinct(self, A, start, end):
        if start > end:
            return -1

        mid = start + (end - start) // 2
        if A[mid] == mid:
            return mid

        # Search left
        leftIndex = min(mid - 1, A[mid])
        left = self.searchNonDistinct(A, start, leftIndex)
        if left >= 0:
            return left

        # Search right
        rightIndex = max(mid + 1, A[mid])
        return self.searchNonDistinct(A, rightIndex, end)

# Example usage
solution = Solution()
print(solution.findMagicIndexDistinct([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13])) 
print(solution.findMagicIndexNonDistinct([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]))

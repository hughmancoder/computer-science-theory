class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
    
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums

        m = len(nums) // 2
        left = nums[:m]
        right = nums[m:]

        left = self.mergeSort(left)
        right = self.mergeSort(right)
        
        return self.merge(left, right)

    def merge(self, left, right):
        l, r = 0, 0
        
        res = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1

        # merge remaining array
        while l < len(left):
            res.append(left[l])
            l += 1

        while r < len(right):
            res.append(right[r])
            r += 1

        return res
        

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
    
    def quickSort(self, nums, lo, hi):
        if hi <= lo:
            return
        
        i = lo
        j = hi
        pivot = nums[(lo + hi) // 2]
        
        while i <= j:
            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
            
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        self.quickSort(nums, lo, j)
        self.quickSort(nums, i, hi)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count_zero = 0
        l = -1
        
        for i in range(0,len(nums)):
            
            if nums[i] == 0:
                count_zero += 1
                if count_zero ==1:
                    l =i
            
            if nums[i] != 0 and count_zero>0:
                nums[l] = nums[i]
                nums[i] = 0
                
                if count_zero > 1:
                    l = l + 1
                else:
                    l = i
                    
        
                
        
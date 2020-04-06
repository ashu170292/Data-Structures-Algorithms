class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [1]
        right =[1]
        result = []
        
        for i in range(1,len(nums)):
            left.append(nums[i-1]*left[i-1])
            right.append(nums[len(nums) -1 - i +1]*right[i-1])
            
        #nums_2 = nums[::-1]
        
        # for j in range(1,len(nums)):
        #     right.append(nums_2[j-1]*right[j-1])
            
        #right = right[::-1]
        
        for k in range(0,len(nums)):
            result.append(right[len(nums) - 1 - k]*left[k])
            
        return result
            
        
        
        
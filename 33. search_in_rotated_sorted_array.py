class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        #O(n) is brute force
        
        left = 0
        right = len(nums)-1
        
        if not nums:
            return -1
        
        # while (left>=0 and left<= len(nums)-1) and (right>=0 and right<= len(nums)-1) :
        while left<=right :
            
            mid = (left + right)//2
            
            if nums[mid] == target:
                
                return mid
            
            elif left==right:
                
                return -1
            
            elif (target < nums[left]) and target > nums[right]:
                
                return -1
            
            else:
                
                #if (nums[mid-1] < nums[mid]) and (nums[mid]>nums[mid+1]):
                if (nums[mid]>nums[mid+1]):
                    if target>nums[mid]:
                        return -1
                    elif (target < nums[mid]) and (target >= nums[left]):
                        right = mid -1
                    elif target <= nums[right]:
                        left = mid + 1
                    
                else:
                    
                    if target > nums[mid]:
                        if nums[mid] >= nums[left] or target <= nums[right]:
                            left = mid + 1
                        else:
                            right = mid - 1
                    else:
                        if nums[mid] < nums[right] or target > nums[right]:
                            right = mid 
                        else:
                            left = mid + 1
                    
                    
                    
        return -1
            
            
        
        
        
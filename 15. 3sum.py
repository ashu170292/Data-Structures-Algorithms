class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        set_results = set()
        cnt =0
        for i,j in enumerate(nums):
            l=0
            r= len(nums)-1
            target = -1*j
            if i>0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    if i==l:
                        l += 1
                    elif i == r:
                        r -= 1
                    else:
                        list_index = [l,r,i]
                        list_index.sort()
                        seq =(nums[list_index[0]],nums[list_index[1]],nums[list_index[2]])
                        if seq not in set_results:
                            set_results.add(seq)
                            cnt += 1
                        if (r-l) > 0:
                            r -= 1
                            l += 1
        
        if cnt > 0:
            res =[]
            for i in set_results:
                res.append(list(i))
            return res
        else:
            return None
            
            
                
                
        
                        
                    
        
        
                    
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right =-1
        dict_seen = {}
        max_so_far = 0
        
        for i,j in enumerate(s):
            if j in dict_seen.keys():
                right = i
                if dict_seen[j] >= left:
                    left = dict_seen[j] + 1
                dict_seen[j] = i
                max_so_far = max(right - left + 1,max_so_far)        
            else:
                right += 1
                max_so_far = max(right - left + 1,max_so_far) 
                dict_seen[j] = i    
        return max_so_far
                
                
                
                
                
                
            
            
            
            
            
        
        
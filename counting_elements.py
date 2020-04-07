class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        dict_nums = {}
        cnt = 0
        
        for i in arr:
            if i in dict_nums.keys():
                dict_nums[i] += 1
            else:
                dict_nums[i] = 1
        
        for key in dict_nums:
            if key+1 in dict_nums.keys():
                cnt = cnt + dict_nums[key]
        
        
        return cnt
                
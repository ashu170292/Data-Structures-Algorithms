class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         dict_sort ={}
#         for i in strs:
#             j = str(sorted(i))
#             if j in dict_sort.keys():
#                 dict_sort[j].append(i)
#             else:
#                 dict_sort[j] = [i]
            
#         return dict_sort.values()
    
        import collections
        res = collections.defaultdict(list)
        
        for i in strs:
            letters = [0] * 26    
            for j in i:
                letters[ord(j) - ord('a')] += 1
            
            res[tuple(letters)].append(i)
            
        return res.values()
                
                
        
        
        
            
            
        
                
        
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1_start = 0
        nums2_start = 0
        final = []
        
        # if (len(nums1)+len(nums2))%2 ==0:
        #     index1 = num 
        
        
        while nums1_start < len (nums1) and nums2_start < len (nums2):
            if nums1[nums1_start] < nums2[nums2_start]:
                final.append(nums1[nums1_start])
                nums1_start +=1
            elif nums1[nums1_start] > nums2[nums2_start]:
                final.append(nums2[nums2_start])
                nums2_start +=1
            else:
                final = final + [nums1[nums1_start],nums2[nums2_start]]
                nums1_start +=1
                nums2_start +=1
            
        # if nums1_start == nums2_start and nums1_start == len(nums1):
        #     return final
        if nums1_start == len(nums1):
            final = final + nums2[nums2_start:len(nums2)]
        else:
            final = final + nums1[nums1_start:len(nums1)]
                
            
        if (len(nums1)+len(nums2))%2 ==0:
            return (final[int(len(final)/2) -1] + final[int(len(final)/2)] )/2
        else:
            #return len(final)
            return final[int((len(final)+1)/2) -1]
                
                
        
                
        
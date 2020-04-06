class Solution:
    def sortArray(self, nums):
        l = 0
        r = len(nums) - 1
        if l < r:
            mid = (l+r) // 2
            arr1 = self.sortArray(nums[l:mid+1])
            print (arr1)
            arr2 = self.sortArray(nums[mid+1:])
            
            print (arr2)
            return self.MergeSortedArrays(arr1,arr2)
        else:
            return nums
    def MergeSortedArrays(self,arr1,arr2):
        if arr1 is None:
            return arr2
        if arr2 is None:
            return arr1
        lst = []
        l1 = 0
        l2 = 0
        while (l1 < len(arr1)) and (l2 < len(arr2)):
            if (arr1[l1]) > (arr2[l2]):
                lst.append(arr2[l2])
                l2 += 1
            else:
                lst.append(arr1[l1])
                l1 += 1    
        if l1 == len(arr1):
            lst.extend(arr2[l2:])
        else:
            lst.extend(arr1[l1:])
        return lst

sol = Solution()
arr = [2,31,8,7,5,4]
print (sol.sortArray(arr))
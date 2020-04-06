class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        i=len(matrix) -1
        j = 0
        while i>=0 and j<len(matrix[0]):
            init = matrix[i][j]
            if init == target:
                return True
            elif init<target:
                j +=1
            else:
                i -= 1    
        return False
            
                
                
                
        
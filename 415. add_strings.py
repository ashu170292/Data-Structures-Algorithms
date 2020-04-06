class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        dict1= {'0':0,
               '1':1,
               '2':2,
               '3':3,
               '4':4,
               '5':5,
               '6':6,
               '7':7,
               '8':8,
               '9':9}
        places1 = len(num1) -1
        num1_int = 0
        for i in num1:
            num1_int += (10**places1 * dict1[i])
            places1 -= 1 
        places2= len(num2)-1
        num2_int = 0
        for j in num2:
            num2_int += (10**places2 * dict1[j])
            places2 -= 1
            
        return str(num1_int + num2_int)
        
            
        
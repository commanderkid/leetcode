#Given a 32-bit signed integer, reverse digits of an integer.

#Example 1:

#Input: 123
#Output:  321
#Example 2:

#Input: -123
#Output: -321
#Example 3:

#Input: 120
#Output: 21
#Note:
#Assume we are dealing with an environment which could 
#only hold integers within the 32-bit signed integer range. 
#For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

#Code

class Solution:
    def reverse(self, x):
        new_str = ""
        self.x = str(x)
        if int(self.x) >= 0:
            for i in range(len(self.x)):
                new_str = new_str + (self.x[(len(self.x)- 1) - i])
            new_str = int(new_str)
        else:
            new_str = "-"
            for i in range(len(self.x)):
                new_str = new_str + (self.x[(len(self.x)- 1) - i])
            new_str = int(new_str)               
        return new_str

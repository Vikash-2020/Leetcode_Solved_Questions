class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x = abs(x)
        reversed = 0
        while(x>0):
            reversed = (reversed*10) + (x%10)
            x = x//10
        if reversed>= -2**31 and reversed<= 2**31 - 1:
            return reversed *sign
        else:
            return 0
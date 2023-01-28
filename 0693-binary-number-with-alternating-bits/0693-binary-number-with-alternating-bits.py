class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # print(not((n&1)^((n>>1)&1)))
        while n>2:
            if not((n&1)^((n>>1)&1)):
                return False
            n=n>>1
        return True
                
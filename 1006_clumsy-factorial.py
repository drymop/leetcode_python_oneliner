class Solution:
    def clumsy(self, n: int) -> int:
        return n<5and[0,1,2,6,7][n]or[1,2,2,-1][n%4]+n

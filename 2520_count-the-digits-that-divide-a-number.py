class Solution:
    def countDigits(self, num: int) -> int:
        return sum(num%int(d)<1for d in"%d"%num)

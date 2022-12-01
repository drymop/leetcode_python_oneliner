class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return sum(c in"aeiouAEIOU"for c in s[:len(s)//2])==sum(c in"aeiouAEIOU"for c in s[len(s)//2:])
